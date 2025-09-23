from typing import Type, Optional
from time import time

from buptmw.constants import UC as UCE
from buptmw.plates.cas import CAS


class UC:
    class Exceptions:
        class NeedCAS(Exception):
            def __init__(self):
                self.message = "Need a BUPT.CAS to init."
                super().__init__(self.message)

    def __init__(self, cas: Optional[Type[CAS]] = None):
        if cas is None or not isinstance(cas, CAS):
            raise self.Exceptions.NeedCAS()
        self.cas = cas
        self._login()

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

    # redirect all undefined methods to self.cas
    def __getattr__(self, name):
        attr = getattr(self.cas, name)
        if callable(attr):
            return attr.__get__(self.cas, type(self.cas))
        else:
            return attr
