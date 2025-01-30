import pytest
from main import count_vowels

def test_only_vowels():
    assert count_vowels("aeiou") == 5
    assert count_vowels("АЕЁИОУЫЭЮЯ") == 10

def test_no_vowels():
    assert count_vowels("bcdfghjklmnpqrstvwxyz") == 0
    assert count_vowels("1234567890") == 0

def test_mixed_characters():
    assert count_vowels("Hello, World!") == 3
    assert count_vowels("Привет, мир!") == 3
    assert count_vowels("PYTHON") == 1
    assert count_vowels("катамаран") == 4
    assert count_vowels("презентация") == 5
    assert count_vowels("ёлки палки") == 4
