import sys

import pytest

# The loop will come to the test function first and then it will go to xfail condition
# if the test function is pass and xfail condition is true it will output xpass as result
# if the test function is fail and xfail condition is true it will output xfail as result
# if the test function is pass and xfail condition is false it will output pass as result
# if the test function is fail and xfail condition is false it will output fail as result

@pytest.mark.xfail(raises=IndexError,reason="known issues as it raises index error")
def test_str05():
    letters = 'abcd'
    num = 1234
    assert letters[7]



@pytest.mark.xfail(sys.platform =='linux',reason="works only in unix")
def test_str06():
    letters = 'abcd'
    num = 1234
    assert letters == 'abcd'