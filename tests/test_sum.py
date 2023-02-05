from pytest import TestCase

def basic_sum(a, b):
    return a+b

def test_sum(TestCase):
    assert basic_sum(2,3) == 5

