from buptmw.credential.cas import CASCredential
from buptmw.auth.cas import CASAuth
from buptmw.app.electric import Electric
from tests.conftest import Config


def test_app_electric(config: Config):
    cred = CASCredential(
        username=config.cas_username,
        password=config.cas_password
    )
    auth = CASAuth(cred)
    app = Electric(auth)
    assert app.check()


def test_app_electric_without_authclass(config: Config):
    cred = CASCredential(
        username=config.cas_username,
        password=config.cas_password
    )
    app = Electric(cred)
    assert app.check()


def test_app_electric_without_authclass_and_credclass(config: Config):
    app = Electric({
        "username": config.cas_username,
        "password": config.cas_password
    })
    assert app.check()
