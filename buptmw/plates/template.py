from abc import ABC, abstractmethod
from typing import TYPE_CHECKING
from requests import Session
from copy import deepcopy


from buptmw.constants import SESSION
if TYPE_CHECKING:
    from buptmw.plates.cas import CAS


class Module(Session, ABC):
    def __init__(self):
        super().__init__()
        self.headers["User-Agent"] = SESSION.USER_AGENT

    @abstractmethod
    def _login(self):
        """ Login this module. """
        pass

class Module_CAS(Module):
    def __init__(self, cas: "CAS" = None):
        from buptmw.plates.cas import CAS
        from buptmw.plates.exception import RequireCAS
    
        if not isinstance(cas, CAS):
            raise RequireCAS()
        super().__init__()
        
        # Copy headers and cookies
        self.headers = deepcopy(cas.headers)
        self.cookies = deepcopy(cas.cookies)
