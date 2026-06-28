from buptmw.credential._base import BaseCredential


class CASCredential(BaseCredential):
    username: str
    password: str
