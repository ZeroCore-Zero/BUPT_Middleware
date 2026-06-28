from buptapis import BUPTAPI

from buptmw.app._base import BaseApp
from buptmw.auth.cas import CASAuth


class UC(BaseApp[CASAuth]):
    def __init__(self, auth: CASAuth) -> None:
        super().__init__(auth)
        self.login()

    def check(self) -> bool:
        resp = self.client.get(BUPTAPI.CAS.STATUS)
        if resp.status_code == 200:
            return True
        return False
