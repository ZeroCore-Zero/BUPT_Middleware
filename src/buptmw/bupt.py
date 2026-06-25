from typing import TypedDict


from buptmw.plates.cas import CAS
from buptmw.plates.uc import UC
from buptmw.plates.ucloud import UCloud
from buptmw.plates.elec import Electric
from buptmw.exception import RequireCASCredential


class CAS_Credential(TypedDict):
    username: str | int
    password: str


class BUPT_Auth:
    def __init__(self, cas: CAS_Credential = None):
        self.cas_credential: CAS_Credential = None
        self.login_CAS(cas)
    
    def login_CAS(self, cas: CAS_Credential = None):
        if cas is not None:
            self.cas_credential = cas

        if self.cas_credential is None:
            raise RequireCASCredential
        self.cas = CAS(cas["username"], cas["password"])

    def get_UC(self) -> UC:
        if not self.cas.check():
            self.login_CAS()
        return UC(self.cas)

    def get_UCloud(self) -> UCloud:
        if not self.cas.check():
            self.login_CAS()
        return UCloud(self.cas)

    def get_Electric(self) -> Electric:
        if not self.cas.check():
            self.login_CAS()
        return Electric(self.cas)
