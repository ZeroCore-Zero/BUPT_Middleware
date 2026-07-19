from base64 import b64encode
from datetime import datetime, timedelta
from http.cookiejar import Cookie
from urllib.parse import quote

from buptapis import BUPTAPI

from buptmw.app._base import BaseApp
from buptmw.auth.cas import CASAuth
from buptmw.credential.cas import CASCredential


class UCloud(BaseApp[CASAuth]):
    user_id: str
    access_token: str
    refresh_token: str
    role_name: str
    loginId: str
    user_name: str
    real_name: str
    avatar: str
    dept_id: str
    identity: str

    def __init__(self, auth: CASAuth | CASCredential | dict) -> None:
        super().__init__(auth)
        self.login()

    def login(self) -> None:
        super().login()
        # get ticket
        self.client.headers["Authorization"] = "Basic " + b64encode("portal:portal_secret".encode()).decode()
        resp = self.client.get(BUPTAPI.UCLOUD.LOGIN, follow_redirects=True)
        resp.raise_for_status()
        ticket = resp.url.params.get("ticket")
        if not ticket:
            raise ValueError("Ticket not found.")

        # get token
        resp = self.client.post(
            BUPTAPI.UCLOUD.TOKEN,
            data={
                "ticket": ticket,
                "grant_type": "third"
            }
        )
        resp.raise_for_status()
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

        self.client.headers["Blade-Auth"] = self.access_token

        # set cookies
        info = self.client.get(BUPTAPI.UCLOUD.INFO).json()["data"]
        current = self.client.get(BUPTAPI.UCLOUD.CURRENT).json()["data"]
        user = self.client.get(BUPTAPI.UCLOUD.USER).json()["data"]

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

        for name, value in cookies.items():
            self.client.cookies.jar.set_cookie(Cookie(
                version=0,
                name=name,
                value=value,
                port=None, port_specified=False,
                domain="ucloud.bupt.edu.cn", domain_specified=True, domain_initial_dot=False,
                path="/", path_specified=True,
                secure=False,
                expires=int((datetime.now() + timedelta(hours=1)).timestamp()),
                discard=False,
                comment=None, comment_url=None,
                rest={},
                rfc2109=False
            ))

    def check(self) -> bool:
        resp = self.client.get(BUPTAPI.UCLOUD.INFO)
        if resp.status_code == 200:
            return True
        return False
