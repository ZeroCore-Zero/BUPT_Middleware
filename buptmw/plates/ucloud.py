from typing import Type, Optional
from urllib.parse import urlparse, parse_qs, quote
from base64 import b64encode
from datetime import datetime, timedelta

from buptmw.constants import UCLOUD as UcloudE
from .cas import CAS


class Ucloud:
    class Exceptions:
        class NeedCAS(Exception):
            def __init__(self):
                self.message = "Need a BUPT.CAS to init."
                super().__init__(self.message)

    def __init__(self, cas: Optional[Type[CAS]] = None):
        if cas is None or not isinstance(cas, CAS):
            raise self.Exceptions.NeedCAS()
        self.cas = cas
        self._login()

    def check(self):
        resp = self.get(
            UcloudE.CHECK,
            headers={"blade-auth": self.access_token}
        )
        if resp.status_code == 200:
            return True
        return False

    def _get_cookies(self):
        info = self.cas.get(
            UcloudE.INFO,
            headers={
                "Authorization": self.authorization,
                "Blade-Auth": self.access_token
            }
        ).json()["data"]
        current = self.cas.get(
            UcloudE.CURRENT,
            headers={
                "Authorization": self.authorization,
                "Blade-Auth": self.access_token
            }
        ).json()["data"]
        user = self.cas.get(
            UcloudE.USER,
            headers={
                "Authorization": self.authorization,
                "Blade-Auth": self.access_token
            }
        ).json()["data"]

        cookies = {}
        cookies["iClass-uuid"] = self.user_id
        cookies["iClass-token"] = self.access_token
        cookies["iClass-refresh_token"] = self.refresh_token
        cookies["iClass-login-meth"] = "icloud"
        cookies["iClass-expert-account"] = self.user_name
        cookies["iClass-real_name"] = quote(self.real_name)
        cookies["iClass-role_name"] = self.role_name
        cookies["iClass-avatar"] = self.avatar
        cookies["iClass-loginId"] = self.loginId
        cookies["iClass-user-info"] = quote(str(info))
        cookies["iClass-current-term"] = quote(str(current))
        cookies["iClass-identity"] = self.identity
        cookies["iClass-user-role"] = quote(str(user[0]))
        cookies["iClass-login-roles"] = quote(str(user))

        for cookie in cookies:
            self.cas.session.cookies.set(
                name=cookie,
                value=cookies[cookie],
                domain="ucloud.bupt.edu.cn",
                expires=(datetime.now() + timedelta(hours=1)).timestamp()
            )
        pass

    def _login(self):
        self.authorization = "Basic " + b64encode("portal:portal_secret".encode()).decode()
        resp = self.cas.get(UcloudE.LOGIN)
        self.ticket = parse_qs(urlparse(resp.url).query)["ticket"][0]
        resp = self.cas.post(
            UcloudE.TOKEN,
            headers={
                "Authorization": self.authorization,
            },
            data={
                "ticket": self.ticket,
                "grant_type": "third"
            }
        )
        data = resp.json()
        self.user_id = data["user_id"]
        self.access_token = data["access_token"]
        self.refresh_token = data["refresh_token"]
        self.role_name = data["role_name"]
        self.loginId = data["loginId"]
        self.user_name = data["user_name"]
        self.real_name = data["real_name"]
        self.avatar = data["avatar"]
        self.dept_id = data["dept_id"]
        self.identity = f"{self.role_name}:{self.dept_id}"
        self._get_cookies()

    # redirect all undefined methods to self.cas
    def __getattr__(self, name):
        attr = getattr(self.cas, name)
        if callable(attr):
            return attr.__get__(self.cas, type(self.cas))
        else:
            return attr
