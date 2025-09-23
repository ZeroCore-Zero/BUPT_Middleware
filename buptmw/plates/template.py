from abc import ABC, abstractmethod
from typing import Optional


from buptmw.plates.cas import CAS


class Module_Require_CAS(ABC):
    class Exceptions:
        class RequireCAS(Exception):
            def __init__(self):
                self.message = "Require CAS instance."
                super().__init__(self.message)

    def __init__(self, cas: Optional[CAS] = None):
        if not isinstance(cas, CAS):
            raise self.Exceptions.RequireCAS()
        self.cas = cas
        self._login()
    
    @abstractmethod
    def _login(self):
        """ Login this module. """
        pass

    @abstractmethod
    def check(self):
        """ Check if session expired. """
        pass

    # redirect all undefined methods to self.cas
    def __getattr__(self, name):
        attr = getattr(self.cas, name)
        if callable(attr):
            return attr.__get__(self.cas, type(self.cas))
        else:
            return attr
