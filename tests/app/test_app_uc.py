from buptmw.credential.cas import CASCredential
from buptmw.auth.cas import CASAuth
from buptmw.app.uc import UC
from tests.conftest import Config


def test_app_uc(config: Config):
    cred = CASCredential(
        username=config.cas_username,
        password=config.cas_password
    )
    auth = CASAuth(cred)
    app = UC(auth)
    assert app.check()
