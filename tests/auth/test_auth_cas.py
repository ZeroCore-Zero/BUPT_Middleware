from buptmw.credential.cas import CASCredential
from buptmw.auth.cas import CASAuth
from tests.conftest import Config


def test_auth_cas(config: Config):
    cred = CASCredential(
        username=config.cas_username,
        password=config.cas_password
    )
    auth = CASAuth(cred)
    assert auth.check()
