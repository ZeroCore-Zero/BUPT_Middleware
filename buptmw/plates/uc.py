from typing import Type, Optional

from ..constants import BUPT_UC_LOGIN
from .cas import CAS


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

    def _login(self):
        self.cas.get(BUPT_UC_LOGIN)

    # redirect all undefined methods to self.cas
    def __getattr__(self, name):
        attr = getattr(self.cas, name)
        if callable(attr):
            return attr.__get__(self.cas, type(self.cas))
        else:
            return attr
