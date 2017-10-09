import pytest


@pytest.fixture
def selenium(selenium):
    selenium.implicity_wait(10)
    selenium.maximize_window()
    return selenium

def test_example(selenium):
    selenium.get('http://www.example.com')