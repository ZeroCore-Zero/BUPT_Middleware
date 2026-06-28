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
