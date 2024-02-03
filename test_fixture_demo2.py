import pytest

@pytest.fixture()
def setup_list():
    city = ["N"]
    return city


def test_usefixturedemo(setup_list):
    assert setup_list == ["N"]