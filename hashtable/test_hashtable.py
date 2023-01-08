from hashtable import HashTable
from random import randint


# Test hash_fun
def test_hash_fun():
    hash_table = HashTable(17, 3)
    for _ in range(10000):
        list1 = [x for x in range(randint(0, 100))]
        for index, _ in enumerate(list1):
            list1[index] = chr(randint(48, 122))
        stroka = ''.join(list1)
        id = hash_table.hash_fun(stroka)
        assert id >= 0
        assert id <= 16


# Test seek_slot
def test_seek_slot_1():
    hash_table = HashTable(17, 3)
    for slot_index, _ in enumerate(hash_table.slots):
        hash_table.slots[slot_index] = 1
    values_covering_all_indexes = 'abcdefghijklmnopq'
    for value in values_covering_all_indexes:
        assert hash_table.seek_slot(value) is None


def test_seek_slot_2():
    length = 15
    step = 3
    hash_table = HashTable(length, step)
    # hash_fun('a') == 7 if length == 15
    a_id = hash_table.hash_fun('a')
    curr_id = a_id + step
    hash_table.slots[a_id] = 1
    while curr_id != a_id:
        hash_table.slots[curr_id] = 1
        curr_id = (curr_id + step) % length
    # The function tries to find a free slot every 'step' slots,
    # but they are all occupied. So we expect None
    assert hash_table.seek_slot('a') is None
    # Also None for ord('a') + step:
    assert hash_table.seek_slot(chr(ord('a') + step)) is None

# Test find
def test_find_1():
    hash_table = HashTable(7, 2)
    stroks = ['bla',
              'bla-bla',
              'bla-bla-bla',
              'stroka4',
              'stroka5',
              'asda',
              'sdfgfds']
    for stroka in stroks:
        hash_table.put(stroka)
    assert hash_table.find('no_stroka') is None
    for stroka in stroks:
        assert 0 <= hash_table.find(stroka) < 7
