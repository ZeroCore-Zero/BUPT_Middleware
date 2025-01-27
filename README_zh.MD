# BUPT_Middleware

[English](./README.MD) | <u>中文</u>

帮助北邮学生更加容易地访问学校系统。

## 功能

- 访问 [CAS](https://auth.bupt.edu.cn/authserver/login)
  - 访问 [UC](https://uc.bupt.edu.cn/#/user/pc/index)
  - 访问 [Ucloud](https://ucloud.bupt.edu.cn/)

## 下载

``` bash
pip install buptmw
```

## 用法

### 通用

获取任何实例后，将其当作`requests.Session`一样来使用，这个库会帮助你自动完成那些烦人的鉴权过程。

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

**重要：获取Ucloud实例之前先获取CAS实例**

``` python
from buptmw import BUPT_Auth

auth = {
    "username": "yourUsername",
    "password": "yourPassword"
}
user = BUPT_Auth(cas=auth)
ucloud = user.get_Ucloud()
```