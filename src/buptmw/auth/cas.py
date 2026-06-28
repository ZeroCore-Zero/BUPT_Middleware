import re

from bs4 import BeautifulSoup
from buptapis import BUPTAPI

from buptmw.auth._base import BaseAuth
from buptmw.credential.cas import CASCredential


class CASAuth(BaseAuth[CASCredential]):
    def __init__(self, credential: CASCredential) -> None:
        super().__init__(credential)
        self.login()

    def login(self) -> None:
        super().login()
        resp = self.client.get(url=BUPTAPI.CAS.LOGIN)
        resp.raise_for_status()
        parsed = BeautifulSoup(resp.text, "lxml")
        execution_input = parsed.find("input", {"name": "execution"})
        if execution_input is None:
            raise ValueError("Execution value not found.")
        
        post_data = {
            "username": self.credential.username,
            "password": self.credential.password,
            "type": "username_password",
            "submit": "LOGIN",
            "_eventId": "submit",
            "execution": execution_input["value"]
        }

        # captcha
        pattern = r"config\.captcha\s*=\s*\{\s*type:\s*'image',\s*id:\s*'(\d+)'\s*\};"
        match = re.search(pattern, resp.text)
        if match:
            captcha_id = match.group(1)
            raise RuntimeError(f"Captcha occured, id {captcha_id}.")

        resp = self.client.post(url=BUPTAPI.CAS.LOGIN, data=post_data, follow_redirects=True)
        resp.raise_for_status()

    def check(self) -> bool:
        resp = self.client.get(BUPTAPI.CAS.STATUS)
        if resp.status_code == 200:
            return True
        return False
