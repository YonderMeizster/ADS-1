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
    while len(array) != 0:
        array.delete(0)
    assert array.capacity >= 16


def test_delete_no_resize_1():
    array = DynArray()
    for i in range(51):
        array.append(i)
    prev_capacity = array.capacity # array.capacity == 64
    array.delete(0)
    assert array.capacity == prev_capacity # capacity shouldn't change


def test_delete_no_resize_2():
    array = DynArray()
    for i in range(16):
        array.append(i)
    for i in range(16):
        array.delete(0)
        assert array.capacity == 16


def test_delete_count_equal_50_percent():
    array = DynArray()
    for i in range(17):
        array.append(i)
    array.delete(0)
    assert array.capacity == 32


def test_delete_count_below_50_percent():
    array = DynArray()
    for i in range(17):
        array.append(i)
    array.delete(0)
    array.delete(0)
    assert array.capacity == 21


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
