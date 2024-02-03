import pytest

@pytest.fixture()
def setup_list():
    city = ['New york','London','Riyadh','singapore','mumbai']
    return city


def test_getItem(setup_list):
    assert setup_list[0] == 'New york'
    assert setup_list[::2] == ['New york','Riyadh','mumbai']


