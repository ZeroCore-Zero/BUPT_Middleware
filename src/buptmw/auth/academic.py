import base64

from buptapis import BUPTAPI

from buptmw.auth._base import BaseAuth
from buptmw.credential.academic import AcademicCredential


class AcademicAuth(BaseAuth[AcademicCredential]):
    def __init__(self, credential: AcademicCredential) -> None:
        super().__init__(credential)
        self.login()

    def login(self) -> None:
        super().login()
        encoded = (
            base64.b64encode(self.credential.username.encode()).decode()
            + r"%%%"
            + base64.b64encode(self.credential.password.encode()).decode()
        )
        post_data = {"encoded": encoded}
        resp = self.client.post(url=BUPTAPI.ACADEMIC.LOGIN, data=post_data, follow_redirects=True)
        resp.raise_for_status()

    def check(self) -> bool:
        resp = self.client.get(BUPTAPI.ACADEMIC.STATUS)
        if resp.status_code == 200:
            return True
        return False
