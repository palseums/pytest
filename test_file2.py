import pytest
pytestmark = pytest.mark.skipif(10 == 10,reason="whole file  is not satisfied")
const1 = 10
class TestHello():
    def test_hello(self):
        assert "palani" == "palani"
    @pytest.mark.skip(reason="skipping for no specific reason")
    def test_exception1(self):
        with pytest.raises(Exception):
            print("hello")
            assert True
    @pytest.mark.skipif(const1 == 10,reason="constant1 is not satisfied")
    @pytest.mark.sanity
    def test_constant(self):
        assert 5+5 == 10
