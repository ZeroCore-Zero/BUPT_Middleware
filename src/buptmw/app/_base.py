from abc import ABC, abstractmethod
from typing import Generic, TypeVar

import httpx

from buptmw.auth._base import BaseAuth

AUTHTYPE = TypeVar("AUTHTYPE", bound="BaseAuth")


class BaseApp(Generic[AUTHTYPE], ABC):
    client: httpx.Client
    auth: AUTHTYPE

    def __init__(self, auth: AUTHTYPE) -> None:
        super().__init__()
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
