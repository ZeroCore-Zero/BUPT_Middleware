from typing import Type

from buptmw.plates.cas import CAS
from buptmw.plates.uc import UC
from buptmw.plates.ucloud import Ucloud


class BUPT_Auth:
    def __init__(self, cas=None):
        self._plates_instance = {}
        self._plates_map = {
            "UC": UC,
            "Ucloud": Ucloud
        }
        if cas is not None:
            self.cas = CAS(cas["username"], cas["password"])

    def _get_instance(self, label):
        plate = self._plates_map[label]
        if label not in self._plates_instance or not self._plates_instance[label].check():
            self._plates_instance[label] = plate(cas=self.cas)
        return self._plates_instance[label]

    def get_UC(self) -> Type[UC]:
        return self._get_instance("UC")

    def get_Ucloud(self) -> Type[Ucloud]:
        return self._get_instance("Ucloud")
