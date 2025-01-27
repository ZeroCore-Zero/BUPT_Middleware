# BUPT_Middleware

<u>English</u> | [中文](./README_zh.MD)

This project aims to help BUPT students simply access school systems with python, without multifarious process.

## Ability

- Access [CAS](https://auth.bupt.edu.cn/authserver/login)
  - Access [UC](https://uc.bupt.edu.cn/#/user/pc/index)
  - Access [Ucloud](https://ucloud.bupt.edu.cn/)

## Download

``` bash
pip install buptmw
```

## Usage

### General

Whenever you get a instance, you can use it as a `requests.Session`, any additional operation like tiresome authentication can be omitted for you.

### CAS

``` python
from buptmw import BUPT_Auth

auth = {
    "username": "yourUsername",
    "password": "yourPassword"
}
user = BUPT_Auth(cas=auth)
```

### Ucloud

**Necessary: Get CAS instance ahead of Ucloud.**

``` python
from buptmw import BUPT_Auth

auth = {
    "username": "yourUsername",
    "password": "yourPassword"
}
user = BUPT_Auth(cas=auth)
ucloud = user.get_Ucloud()
```