from buptapis import BUPTAPI

from buptmw.app._base import BaseApp
from buptmw.auth.cas import CASAuth
from buptmw.credential.cas import CASCredential


class Electric(BaseApp[CASAuth]):
    def __init__(self, auth: CASAuth | CASCredential | dict) -> None:
        super().__init__(auth)
        self.login()
    
    def login(self) -> None:
        super().login()
        resp = self.client.get(BUPTAPI.ELECTRIC.LOGIN, follow_redirects=True)
        resp.raise_for_status()

    def check(self) -> bool:
        resp = self.client.get(BUPTAPI.ELECTRIC.HOMEPAGE)
        if resp.status_code == 200:
            return True
        return False
