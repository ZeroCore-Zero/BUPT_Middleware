from buptapis import BUPTAPI

from buptmw.app._base import BaseApp
from buptmw.auth.academic import AcademicAuth
from buptmw.credential.academic import AcademicCredential


class Academic(BaseApp[AcademicAuth]):
    def __init__(self, auth: AcademicAuth | AcademicCredential | dict) -> None:
        super().__init__(auth)
        self.login()

    def check(self) -> bool:
        resp = self.client.get(BUPTAPI.ACADEMIC.STATUS)
        if resp.status_code == 200:
            return True
        return False
