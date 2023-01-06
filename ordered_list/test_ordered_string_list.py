from ordered_list import OrderedStringList


# Add tests
def test_add_ascending1():
    order1 = OrderedStringList(asc = True)
    order1.add('b')
    order1.add('c')
    order1.add('a')
    assert order1._get_all_debug() == ['a', 'b', 'c']


def test_add_ascending_2():
    order1 = OrderedStringList(asc = True)
    order1.add('a')
    order1.add('b')
    order1.add('c')
    order1.add('a')
    order1.add('a')
    order1.add('c')
    order1.add('c')
    order1.add('b')
    order1.add('b')
    assert order1._get_all_debug() == ['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'c']


def test_add_descending_1():
    order1 = OrderedStringList(asc = False)
    order1.add('b')
    order1.add('a')
    order1.add('c')
    assert order1._get_all_debug() == ['c', 'b', 'a']


def test_add_descending_2():
    order1 = OrderedStringList(asc = False)
    order1.add('c')
    order1.add('b')
    order1.add('a')
    order1.add('c')
    order1.add('a')
    order1.add('b')
    order1.add('c')
    order1.add('a')
    order1.add('b')
    assert order1._get_all_debug() == ['c', 'c', 'c', 'b', 'b', 'b', 'a', 'a', 'a']
