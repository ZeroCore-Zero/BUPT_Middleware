from bs4 import BeautifulSoup


from buptmw.plates.template import Module
from buptmw.constants import CAS as CASE
from buptmw.utils.auto_retry import auto_retry_network_connections


class CAS(Module):
    def __init__(self, username, password):
        super().__init__()
        self._login(username, password)

    @auto_retry_network_connections
    def _login(self, username, password):
        resp = self.get(url=CASE.LOGIN)
        parsed = BeautifulSoup(resp.text, "lxml")
        varid = parsed.find(attrs={"name": "execution"})["value"]
        post_data = {
            "username": username,
            "password": password,
            "type": "username_password",
            "submit": "LOGIN",
            "_eventId": "submit",
            "execution": varid
        }

        # captcha
        captcha = parsed.find(id="captcha")
        if captcha:
            captcha_img = captcha.find("img").get("src")
            print(captcha_img)

        resp = self.post(url=CASE.LOGIN, data=post_data)
        resp.raise_for_status()


    def check(self):
        resp = self.get(CASE.LOGIN, allow_redirects=False)
        if resp.status_code == 302:
            return True
        return False
