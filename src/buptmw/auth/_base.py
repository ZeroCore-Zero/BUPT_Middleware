from abc import ABC, abstractmethod
from typing import Generic, TypeVar

import httpx

from buptmw.credential._base import BaseCredential

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/131.0.0.0 Safari/537.36"
)
CREDTYPE = TypeVar("CREDTYPE", bound="BaseCredential")


class BaseAuth(Generic[CREDTYPE], ABC):
    client: httpx.Client
    credential: CREDTYPE

    def __init__(self, credential: CREDTYPE) -> None:
        super().__init__()
        self.credential = credential

    def login(self) -> None:
        """Perform authentication login."""
        if hasattr(self, "client"):
            self.client.close()
        self.client = httpx.Client()
        self.client.headers["User-Agent"] = USER_AGENT

    @abstractmethod
    def check(self) -> bool:
        """Check if the session is still valid."""
        pass

    def get_client(self) -> httpx.Client:
        """Return the client if session is valid, else relogin firstly."""
        if not hasattr(self, "client") or not self.check():
            self.login()
        return self.client
