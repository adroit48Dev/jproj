import pytest


def basic_sum(a, b):
    return a+b

def test_sum():
    assert basic_sum(2,3) == 5

