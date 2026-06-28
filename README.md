# BUPT_Middleware

[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/ZeroCore-Zero/BUPT_Middleware)

This project aims to help BUPT students simply access school systems with python, without authentication process manually.

## Supported

- Access [CAS](https://auth.bupt.edu.cn/authserver/login)
  - Access [UC](https://uc.bupt.edu.cn/#/user/pc/index)
  - Access [UCloud](https://ucloud.bupt.edu.cn/)
  - Access [Electric](https://app.bupt.edu.cn/buptdf/wap/default/chong/)
- Access [Academic](https://jwgl.bupt.edu.cn/jsxsd/)

## Install

``` bash
pip install buptmw
```

## Usage

Follow the **Credential**->**Auth**->**App** layout chain, and call `get_client()` to get a verified `httpx.Client`, which you can use to make requests. Any tiresome authentication can be omitted for you.

``` python
from buptmw import CASCredential, CASAuth, UCloud

cred = CASCredential(username="yourUsername", password="yourPassword")
auth = CASAuth(cred)
app = UCloud(auth)

client = app.get_client()
response = client.get("https://someurl")
# do something with response
```

> [!IMPORTANT]
> 
> Always use `get_client()` to obtain the client before making requests. It will automatically check and refresh the session if it has expired.
