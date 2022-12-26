import pytest
from dynarray import DynArray


# Insert tests
def test_insert_into_empty():
    array = DynArray()
    array.insert(0, 1)


def test_insert_into_begin():
    array = DynArray()
    for i in range(5):
        array.insert(0, i)
    assert array.__str__() == '4, 3, 2, 1, 0'
    

def test_insert_into_end():
    array = DynArray()
    for i in range(5):
        array.insert(i, i)
    assert array.__str__() == '0, 1, 2, 3, 4'


def test_insert_into_middle():
    array = DynArray()
    for i in range(5):
        array.insert(i // 2, i)
    assert array.__str__() == '1, 3, 4, 2, 0'


def test_insert_resize():
    array = DynArray()
    prev_capasity = array.capacity
    for i in range(prev_capasity):
        array.insert(i, i)
    assert array.capacity == prev_capasity
    array.insert(16, 1)
    assert array.capacity == prev_capasity * 2


def test_insert_no_resize():
    array = DynArray()
    prev_capasity = array.capacity
    for i in range(prev_capasity - 1):
        array.insert(i, i)
    assert array.capacity == prev_capasity


def test_insert_below_bounds():
    array = DynArray()
    for i in range(5):
        array.insert(i, i)
    with pytest.raises(IndexError):
        array.insert(-1, 1)


def test_insert_under_bounds():
    array = DynArray()
    for i in range(5):
        array.insert(i, i)
    with pytest.raises(IndexError):
        array.insert(array.count + 1, 1)


# Delete tests
def test_delete_empty():
    array = DynArray()
    with pytest.raises(IndexError):
        array.delete(0)


def test_delete_all():
    array = DynArray()
    for i in range(10):
        array.append(i)
    while len(array) != 0:
        array.delete(0)
    assert len(array) == 0


def test_delete_all_capasity_still_16():
    array = DynArray()
    for i in range(100):
        array.append(i)
    assert array.capacity == 128
    while len(array) != 0:
        array.delete(0)
    assert array.capacity == 16


def test_delete_resize():
    array = DynArray()
    for i in range(17):
        array.append(i)
    assert array.capacity == 32
    array.delete(0)
    assert array.capacity == 21 # int(32 / 1.5)


def test_delete_capasity_greater_than_16():
    array = DynArray()
    array.append(1)
    array.capacity = 20 # dirty hack
    array.delete(0)
    assert array.capacity == 20


def test_delete_capasity_equal_16():
    array = DynArray()
    array.append(1)
    array.capacity = 24 # dirty hack
    array.delete(0)
    assert array.capacity == 16


def test_delete_below_bounds():
    array = DynArray()
    for i in range(5):
        array.insert(i, i)
    with pytest.raises(IndexError):
        array.delete(-1)


def test_delete_under_bounds():
    array = DynArray()
    for i in range(5):
        array.insert(i, i)
    with pytest.raises(IndexError):
        array.delete(len(array))