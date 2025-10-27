from typing import Optional


from buptmw.constants import ELEC as ELECE
from buptmw.plates.cas import CAS
from buptmw.plates.template import Module_Require_CAS


class Elec(Module_Require_CAS):
    def __init__(self, cas: Optional[CAS] = None):
        super().__init__(cas)

    def _login(self):
        self.get(ELECE.LOGIN)
    
    def check(self):
        resp = self.get(ELECE.CHECK)
        if resp.status_code == 200:
            return True
        return False
