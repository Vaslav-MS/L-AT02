import pytest
from main import check

def test_check_2():
    assert check(6) == True

def test_check_1():
    assert check(5) == False

@pytest.mark.parametrize('num,expected', [
    (2, True),
    (5, False),
    (0, True),
    (56, True),
    (-3, False),
    (-100, True)
])

def test_check_with_param(num, expected):
   assert check(num) == expected


