from typing import Type

from buptmw.bupt import BUPT_Auth
from buptmw.plates.cas import CAS
from buptmw.plates.uc import UC
from buptmw.plates.ucloud import Ucloud

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