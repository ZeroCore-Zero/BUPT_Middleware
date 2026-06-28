from buptmw.credential.academic import AcademicCredential
from buptmw.auth.academic import AcademicAuth
from buptmw.app.academic import Academic
from tests.conftest import Config


def test_app_academic(config: Config):
    cred = AcademicCredential(
        username=config.academic_username,
        password=config.academic_password
    )
    auth = AcademicAuth(cred)
    app = Academic(auth)
    assert app.check()
