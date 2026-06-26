from buptapis import BUPTAPI
from buptmw.plates.cas import CAS
from buptmw.plates.template import Module_CAS


class UC(Module_CAS):
    def __init__(self, cas: CAS):
        super().__init__(cas)
        self._login()

    def _login(self):
        self.get(BUPTAPI.CAS.LOGIN)
