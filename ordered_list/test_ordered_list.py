from ordered_list import OrderedList


# Add tests
def test_add_ascending():
    order1 = OrderedList(asc = True)
    for i in range(5, -6, -1):
        order1.add(i)
    assert order1._get_all_debug() == [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]


def test_add_descending():
    order1 = OrderedList(asc = False)
    for i in range(-5, 6):
        order1.add(i)
    assert order1._get_all_debug() == [5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5]


def test_add_ascending_head():
    order1 = OrderedList(asc = True)
    order1.add(1)
    order1.add(1)
    order1.add(1)
    order1.add(0)
    assert order1.head.value == 0
    assert order1.head.prev is None
    assert order1.head.next.value == 1


def test_add_ascending_tail():
    order1 = OrderedList(asc = True)
    order1.add(1)
    order1.add(1)
    order1.add(1)
    order1.add(2)
    assert order1.tail.value == 2
    assert order1.tail.next is None
    assert order1.tail.prev.value == 1


def test_add_ascending_middle():
    order1 = OrderedList(asc = True)
    order1.add(1)
    order1.add(3)
    order1.add(2)
    assert order1._get_all_debug() == [1, 2, 3]
    assert order1.head.prev is None
    assert order1.tail.next is None


#Tests clean
def test_clean_empty():
    order1 = OrderedList(asc = True)
    assert order1._OrderedList__ascending == True
    order1.clean(asc = False)
    assert order1._OrderedList__ascending == False


def test_clean():
    order1 = OrderedList(asc = False)
    order1.add(5)
    order1.add(3)
    order1.add(8)
    assert order1._get_all_debug() == [8, 5, 3]
    order1.clean(asc = True)
    assert order1.len() == 0
    assert order1.head is None
    assert order1.tail is None
    order1.add(5)
    order1.add(3)
    order1.add(8)
    assert order1._get_all_debug() == [3, 5, 8]


#Tests find
def test_find_empty():
    order1 = OrderedList(asc = True)
    assert order1.find(2) is None


def test_find_asc():
    order1 = OrderedList(asc = True)
    order1.add(1)
    order1.add(2)
    order1.add(3)
    order1.add(4)
    order1.add(1)
    assert order1.find(1).value == 1
    assert order1.find(6) is None


def test_find_des():
    order1 = OrderedList(asc = False)
    order1.add(1)
    order1.add(2)
    order1.add(3)
    order1.add(4)
    order1.add(1)
    assert order1.find(1).value == 1
    assert order1.find(6) is None


#Tests delete
def test_delete_empty():
    order1 = OrderedList(asc = True)
    order1.delete(1)


def test_delete_head_is_tail():
    order1 = OrderedList(asc = True)
    order1.add(1)
    order1.delete(1)
    assert order1.head is None
    assert order1.tail is None   
    

def test_delete_head_asc():
    order1 = OrderedList(asc = True)
    order1.add(1)
    order1.add(2)
    order1.delete(1)
    assert order1._get_all_debug() == [2]


def test_delete_head_des():
    order1 = OrderedList(asc = True)
    order1.add(1)
    order1.add(2)
    order1.delete(2)
    assert order1._get_all_debug() == [1]


def test_delete_tail_asc():
    order1 = OrderedList(asc = True)
    order1.add(1)
    order1.add(2)
    order1.delete(2)
    assert order1._get_all_debug() == [1]


def test_delete_tail_des():
    order1 = OrderedList(asc = True)
    order1.add(1)
    order1.add(2)
    order1.delete(1)
    assert order1._get_all_debug() == [2]


def test_delete_middle_asc():
    order1 = OrderedList(asc = True)
    order1.add(1)
    order1.add(2)
    order1.add(2)
    order1.add(2)
    order1.add(3)
    order1.delete(2)
    assert order1._get_all_debug() == [1, 2, 2, 3]


def test_delete_middle_des():
    order1 = OrderedList(asc = False)
    order1.add(1)
    order1.add(2)
    order1.add(2)
    order1.add(2)
    order1.add(3)
    order1.delete(2)
    assert order1._get_all_debug() == [3, 2, 2, 1]


def test_delete_not_found():
    order1 = OrderedList(asc = False)
    order1.add(1)
    order1.add(2)
    order1.add(2)
    order1.add(2)
    order1.add(3)
    order1.delete(0)
    assert order1._get_all_debug() == [3, 2, 2, 2, 1]
