from typing import Type

from .bupt import BUPT_Auth
from .plates.cas import CAS
from .plates.uc import UC
from .plates.ucloud import Ucloud

Type_BUPT_Auth = Type[BUPT_Auth]
Type_CAS = Type[CAS]
Type_UC = Type[UC]
Type_Ucloud = Type[Ucloud]

__all__ = [
    "Type_BUPT_Auth",
    "Type_CAS",
    "Type_UC",
    "Type_Ucloud"
]