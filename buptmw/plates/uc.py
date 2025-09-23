from typing import Optional
from time import time

from buptmw.constants import UC as UCE
from buptmw.plates.cas import CAS
from buptmw.plates.template import Module_Require_CAS


class UC(Module_Require_CAS):
    def __init__(self, cas: Optional[CAS] = None):
        super.__init__(cas)

        # get personal info and store it in self.
        resp = self.get(
            UCE.CHECK,
            params={"selfTimestamp": int(time() * 1000)}
        )
        data = resp.json()["data"]
        self.name = data["name"]
        self.buptid = data["schoolid"]

    def _login(self):
        self.cas.get(UCE.LOGIN)

    def check(self):
        resp = self.get(
            UCE.CHECK,
            params={"selfTimestamp": int(time() * 1000)}
        )
        code = resp.json()["code"]
        if code == 0:
            return True
        return False

