import pytest
from main import check, is_palindrom

def test_is_palindrom_true():
    assert is_palindrom('madam') == True

def test_is_palindrom_false():
    assert is_palindrom('bot') == False

@pytest.mark.parametrize("test_input, expected", [
    ('level', True),
    ('python', False),
    ('racecar', True),
    ('', True),
])

def test_isPalindrome(test_input, expected):
    assert is_palindrom(test_input) == expected


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


