from buptmw.constants import ELEC as ELECE
from buptmw.plates.cas import CAS
from buptmw.plates.template import Module_CAS


class Elec(Module_CAS):
    def __init__(self, cas: CAS = None):
        super().__init__(cas)
        self._login()

    def _login(self):
        self.get(ELECE.LOGIN)
