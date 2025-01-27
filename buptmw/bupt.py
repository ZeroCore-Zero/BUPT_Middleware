from typing import Type

from .plates.cas import CAS
from .plates.uc import UC
from .plates.ucloud import Ucloud


class BUPT_Auth:
    def __init__(self, cas=None):
        self._plates = {}
        if cas is not None:
            self.cas = CAS(cas["username"], cas["password"])

    def get_UC(self) -> Type[UC]:
        label = "UC"
        if label not in self._plates:
            self._plates[label] = UC(cas=self.cas)
        return self._plates[label]

    def get_Ucloud(self) -> Type[Ucloud]:
        label = "Ucloud"
        if label not in self._plates:
            self._plates[label] = Ucloud(cas=self.cas)
        return self._plates[label]
