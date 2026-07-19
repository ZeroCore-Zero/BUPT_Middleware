from abc import ABC, abstractmethod
from typing import get_args, Generic, TypeVar

import httpx

from buptmw.auth._base import BaseAuth
from buptmw.credential._base import BaseCredential

AUTHTYPE = TypeVar("AUTHTYPE", bound="BaseAuth")


class BaseApp(Generic[AUTHTYPE], ABC):
    client: httpx.Client
    auth: AUTHTYPE

    auth_class: type[AUTHTYPE]
    cred_class: type[BaseCredential]

    def __init_subclass__(cls, **kwargs) -> None:
        super().__init_subclass__(**kwargs)
        cls.auth_class = get_args(cls.__orig_bases__[0])[0]
        cls.cred_class = get_args(cls.auth_class.__orig_bases__[0])[0]

    def __init__(self, auth: AUTHTYPE | BaseCredential | dict) -> None:
        super().__init__()
        if isinstance(auth, dict):
            auth = self.cred_class(**auth)
        if isinstance(auth, BaseCredential):
            auth = self.auth_class(auth)
        self.auth = auth

    def login(self) -> None:
        """Perform authentication login."""
        if hasattr(self, "client"):
            self.client.close()
        auth_client = self.auth.get_client()
        self.client = httpx.Client(
            cookies=dict(auth_client.cookies),
            headers=auth_client.headers.copy()
        )

    @abstractmethod
    def check(self) -> bool:
        """Check if the app session is still valid."""
        pass

    def get_client(self) -> httpx.Client:
        """Return the client if session is valid, else relogin firstly."""
        if not hasattr(self, "client") or not self.check():
            self.login()
        return self.client
