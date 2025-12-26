import pytest
import time 

@pytest.fixture
def predict():
    login = f"test_{time.time()}@gmail.com"
    password = f"{time.time()}"
    return login, password