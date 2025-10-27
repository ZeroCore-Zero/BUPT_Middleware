# BUPT_Middleware

This project aims to help BUPT students simply access school systems with python, without multifarious process.

## Ability

- Access [CAS](https://auth.bupt.edu.cn/authserver/login)
  - Access [UC](https://uc.bupt.edu.cn/#/user/pc/index)
  - Access [Ucloud](https://ucloud.bupt.edu.cn/)
  - Access [Electric](https://app.bupt.edu.cn/buptdf/wap/default/chong/)

## Download

``` bash
pip install buptmw
```

## Usage

Before start, you need to pass your **BUPT credential**, which was used in [CAS](https://auth.bupt.edu.cn/authserver/login) to the core class, e.g.

``` python
from buptmw import BUPT_Auth

auth = {
    "username": "yourUsername",
    "password": "yourPassword"
}
user = BUPT_Auth(cas=auth)
```

Then you can call several method to get a verified entity, which you can use it as a `requests.Session`, and any additional operation like tiresome authentication can be omitted for you. For example,

``` python
from buptmw import BUPT_Auth

auth = {
    "username": "yourUsername",
    "password": "yourPassword"
}
user = BUPT_Auth(cas=auth)
ucloud = user.get_Ucloud()
response = ucloud.get("https://someurl")
# do something with response
```

> [!IMPORTANT]
> 
> DO NOT storage the entities which was obtained by `get_xxx` methods directly, because the cookies will expired but this entity can't detect it timely.
>
> Use the `get_xxx` methods when you try to get a session.
