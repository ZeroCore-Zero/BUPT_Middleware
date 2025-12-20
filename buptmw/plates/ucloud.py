from typing import Optional
from urllib.parse import urlparse, parse_qs, quote
from base64 import b64encode
from datetime import datetime, timedelta

from buptmw.constants import UCLOUD as UCLOUDE
from buptmw.plates.cas import CAS
from buptmw.plates.template import Module_CAS


class Ucloud(Module_CAS):
    def __init__(self, cas: Optional[CAS] = None):
        super().__init__(cas)
        self._login()

    def _get_cookies(self):
        info = self.get(UCLOUDE.INFO).json()["data"]
        current = self.get(UCLOUDE.CURRENT).json()["data"]
        user = self.get(UCLOUDE.USER).json()["data"]

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
            self.cookies.set(
                name=cookie,
                value=cookies[cookie],
                domain="ucloud.bupt.edu.cn",
                expires=(datetime.now() + timedelta(hours=1)).timestamp()
            )

    def _login(self):
        self.headers["Authorization"] = "Basic " + b64encode("portal:portal_secret".encode()).decode()
        resp = self.get(UCLOUDE.LOGIN)

        self.ticket = parse_qs(urlparse(resp.url).query)["ticket"][0]
        resp = self.post(
            UCLOUDE.TOKEN,
            data={
                "ticket": self.ticket,
                "grant_type": "third"
            }
        )
        data = resp.json()
        
        self.user_id = data["user_id"]
        self.access_token = data["access_token"]
        self.refresh_token = data["refresh_token"]
        self.role_name = data["currentRole"]
        self.loginId = data["loginId"]
        self.user_name = data["user_name"]
        self.real_name = data["real_name"]
        self.avatar = data["avatar"]
        self.dept_id = data.get("dept_id", "undefinded")
        self.identity = f"{self.role_name}:{self.dept_id}"

        self.headers["Blade-Auth"] = self.access_token
        self._get_cookies()
