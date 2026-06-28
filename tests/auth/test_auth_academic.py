from buptmw.credential.academic import AcademicCredential
from buptmw.auth.academic import AcademicAuth
from tests.conftest import Config

def test_auth_academic(config: Config):
    cred = AcademicCredential(
        username=config.academic_username,
        password=config.academic_password
    )
    auth = AcademicAuth(cred)
    assert auth.check()
