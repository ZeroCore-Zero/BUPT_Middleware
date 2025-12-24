# BUPT_Middleware

[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/ZeroCore-Zero/BUPT_Middleware)

This project aims to help BUPT students simply access school systems with python, without authentication process manually.

## Ability

- Access [CAS](https://auth.bupt.edu.cn/authserver/login)
  - Access [UC](https://uc.bupt.edu.cn/#/user/pc/index)
  - Access [UCloud](https://ucloud.bupt.edu.cn/)
  - Access [Electric](https://app.bupt.edu.cn/buptdf/wap/default/chong/)

## Install

``` bash
pip install buptmw
```

## Usage

Before start, pass your **BUPT Credential** that you needed, which was used in below sites:

1. [CAS](https://auth.bupt.edu.cn/authserver/login)

to the `BUPT_Auth`.

``` python
from buptmw import BUPT_Auth, CAS_Credential

auth: CAS_Credential = {
    "username": "yourUsername",
    "password": "yourPassword"
}
user = BUPT_Auth(cas=auth)
```

Then you can call methods like `get_xxx` to get a verified entity, which you can use it as a `requests.Session`, and any tiresome authentication can be omitted for you.

``` python
from buptmw import BUPT_Auth, CAS_Credential

auth: CAS_Credential = {
    "username": "yourUsername",
    "password": "yourPassword"
}
user = BUPT_Auth(cas=auth)
ucloud = user.get_UCloud()
response = ucloud.get("https://someurl")
# do something with response
```

> [!IMPORTANT]
> 
> DO NOT storage the entities which was obtained by `get_xxx` methods directly, because the cookies will expired but this entity can't detect it timely.
>
> Use the `get_xxx` methods when you try to get a session.
