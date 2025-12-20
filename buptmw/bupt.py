from typing import TypedDict


from buptmw.plates.cas import CAS
from buptmw.plates.uc import UC
from buptmw.plates.ucloud import Ucloud
from buptmw.plates.elec import Elec


class CAS_Credential(TypedDict):
    username: str | int
    password: str


class BUPT_Auth:
    def __init__(self, cas: CAS_Credential = None):
        if cas is not None:
            self.cas = CAS(cas["username"], cas["password"])

    def get_UC(self) -> UC:
        return UC(self.cas)

    def get_Ucloud(self) -> Ucloud:
        return Ucloud(self.cas)

    def get_Elec(self) -> Elec:
        return Elec(self.cas)
