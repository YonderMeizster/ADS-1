from powerset import PowerSet
import time
import random
import string


# Test put
def test_put_1():
    pwset = PowerSet()
    pwset.put('1')
    assert pwset._get_all()['values'] == ['1']


def test_put_3():
    pwset = PowerSet()
    for i in range(20000):
        pwset.put(str(i))
    for i in range(20000):
        pwset.put(str(i))
    assert pwset.size() == 20000


def test_put_dublicates():
    pwset = PowerSet()
    pwset.put('1')
    assert pwset.get('1')
    pwset.put('1')
    assert pwset.size() == 1


# Test remove
def test_remove_1():
    pwset = PowerSet()
    for i in range(20000):
        pwset.put(str(i))
    for i in range(20000):
        assert pwset.remove(str(i)) is True
    assert pwset.size() == 0


def test_remove_2():
    pwset = PowerSet()
    pwset.put('1')
    assert pwset.remove('2') is False
    assert pwset.size() == 1