# ToDo List

## App Fast Creating

Creating App without Auth or Auth&Credential previously.

``` python
from buptmw import AcademicCredential, Academic

app = Academic(AcademicCredential())
app = Academic({"username": "xxx", "password": "xxx"})
```

## Cookie Credential

Supporting creating of Credential with cookies without session-keepalive feature.

``` python
class CASCredential(BaseModel):
    """
    Must provide at lease one of the (username, password) or cookies.
    If both are provided, cookies will be ignore.
    """
    username: str | None = None
    password: str | None = None
    cookies: str | None = None

    @model_validator(mode='after')
    def validate_auth(self):
        basic_auth_status = [self.username, self.password].count(None)
        if basic_auth_status == 0:
            self.cookies = None
            return self
        
        if basic_auth_status == 1:
            raise ValueError("Incorrect credentials.")
        
        if self.cookies is None:
            raise ValueError("Empty credentials.")
        return self
```

Also supporting fast creating with cookies.

``` python
from buptmw import AcademicCredential, Academic

app = Academic({"cookies": "xxx"})
```
