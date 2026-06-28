import os
from pathlib import Path

import pytest
from dotenv import load_dotenv

env_path = Path(__file__).parent.parent / ".env"
if env_path.exists():
    load_dotenv(env_path)
else:
    load_dotenv()


class Config:
    cas_username: str
    cas_password: str
    academic_username: str
    academic_password: str

    def __init__(self):
        self.cas_username = os.getenv("CAS_USERNAME", "")
        self.cas_password = os.getenv("CAS_PASSWORD", "")
        self.academic_username = os.getenv("ACADEMIC_USERNAME", "")
        self.academic_password = os.getenv("ACADEMIC_PASSWORD", "")
        self._validate()
    
    def _validate(self):
        required = {
            "CAS_USERNAME": self.cas_username,
            "CAS_PASSWORD": self.cas_password,
            "ACADEMIC_USERNAME": self.academic_username,
            "ACADEMIC_PASSWORD": self.academic_password
        }
        
        missing = [name for name, value in required.items() if not value]
        if missing:
            pytest.skip(f"Missing config: {missing}")

@pytest.fixture(scope="session")
def config():
    return Config()
