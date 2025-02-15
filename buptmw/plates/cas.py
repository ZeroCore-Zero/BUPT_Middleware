from bs4 import BeautifulSoup
import requests

from buptmw.constants import Session, CAS as CASE
from buptmw.utlis.auto_retry import auto_retry_network_connections


class CAS:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self._history = []
        try:
            self._login()
        except requests.HTTPError as e:
            if e.response.status_code not in [401, 423]:
                raise e
            self.status = False
        else:
            self.status = True

    def _get_session(self):
        session = requests.Session()
        session.headers["User-Agent"] = Session.USER_AGENT
        return session

    @auto_retry_network_connections
    def _login(self):
        self.session = self._get_session()
        resp = self.session.get(url=CASE.LOGIN)
        varid = BeautifulSoup(
            resp.text, "lxml"
        ).find(attrs={"name": "execution"})["value"]
        post_data = {
            "username": self.username,
            "password": self.password,
            "type": "username_password",
            "submit": "LOGIN",
            "_eventId": "submit",
            "execution": varid
        }
        resp = self.session.post(url=CASE.LOGIN, data=post_data)
        resp.raise_for_status()

    # redirect all undefined methods to self.session
    def __getattr__(self, name):
        attr = getattr(self.session, name)
        if callable(attr):
            return attr.__get__(self.session, type(self.session))
        else:
            return attr
