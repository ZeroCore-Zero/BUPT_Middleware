from enum import StrEnum


class Session(StrEnum):
    USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"


class CAS(StrEnum):
    LOGIN = "https://auth.bupt.edu.cn/authserver/login"


class UC(StrEnum):
    LOGIN = "https://uc.bupt.edu.cn/api/login?target=https://uc.bupt.edu.cn/#/user/login"
    CHECK = "https://uc.bupt.edu.cn/api/uc/status"


class UCLOUD(StrEnum):
    LOGIN = "https://auth.bupt.edu.cn/authserver/login?service=http://ucloud.bupt.edu.cn"
    TOKEN = "https://apiucloud.bupt.edu.cn/ykt-basics/oauth/token"
    INFO = "https://apiucloud.bupt.edu.cn/ykt-basics/info"
    CURRENT = "https://apiucloud.bupt.edu.cn/ykt-site/base-term/current"
    USER = "https://apiucloud.bupt.edu.cn/ykt-basics/userroledomaindept/listByUserId"
    CHECK = "https://apiucloud.bupt.edu.cn/blade-portal/home-page-info/getShufflingWebList"
