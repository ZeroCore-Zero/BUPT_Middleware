from buptmw.credential.cas import CASCredential
from buptmw.auth.cas import CASAuth
from buptmw.app.ucloud import UCloud
from tests.conftest import Config


def test_app_ucloud(config: Config):
    cred = CASCredential(
        username=config.cas_username,
        password=config.cas_password
    )
    auth = CASAuth(cred)
    app = UCloud(auth)
    assert app.check()


def test_app_ucloud_without_authclass(config: Config):
    cred = CASCredential(
        username=config.cas_username,
        password=config.cas_password
    )
    app = UCloud(cred)
    assert app.check()


def test_app_ucloud_without_authclass_and_credclass(config: Config):
    app = UCloud({
        "username": config.cas_username,
        "password": config.cas_password
    })
    assert app.check()

