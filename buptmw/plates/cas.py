from bs4 import BeautifulSoup


from buptmw.plates.template import Module
from buptmw.constants import CAS as CASE
from buptmw.utlis.auto_retry import auto_retry_network_connections


class CAS(Module):
    def __init__(self, username, password):
        super().__init__()
        self.username = username
        self.password = password
        self._login()

    @auto_retry_network_connections
    def _login(self):
        resp = self.get(url=CASE.LOGIN)
        parsed = BeautifulSoup(resp.text, "lxml")
        varid = parsed.find(attrs={"name": "execution"})["value"]
        post_data = {
            "username": self.username,
            "password": self.password,
            "type": "username_password",
            "submit": "LOGIN",
            "_eventId": "submit",
            "execution": varid
        }

        resp = self.post(url=CASE.LOGIN, data=post_data)
        resp.raise_for_status()
