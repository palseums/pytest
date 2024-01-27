import pytest


@pytest.fixture(params=[(3,4),[3,5]],ids=['tuple','list'])
def setup01(request):
    return request.param

@pytest.fixture(params=["access","slice","assign","len"])
def setup02(request):
    return request.param



def test_fixture_param01(setup01,setup02):
    # assert (type(setup01)) in ['int']
    assert 1