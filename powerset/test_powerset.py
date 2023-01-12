from powerset import PowerSet


# Test put
def test_put_1():
    pwset = PowerSet()
    pwset.put('1')
    assert pwset._get_all() == ['1']


def test_put_2():
    pwset = PowerSet()    
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


# Test intersection
def test_inter_1():
    set1 = PowerSet()
    set2 = PowerSet()
    for i in range(20000):
        set1.put(str(i))
        set2.put(str(i))
    assert set1.intersection(set2).size() == 20000


def test_inter_2():
    set1 = PowerSet()
    set2 = PowerSet()
    for i in range(20000):
        set1.put(str(i))
    assert set1.intersection(set2).size() == 0


def test_inter_3():
    set1 = PowerSet()
    set2 = PowerSet()
    for i in range(40000):
        set1.put(str(i))
    for i in range(0, 20000):
        set2.put(str(i))
    assert set1.intersection(set2).size() == 20000


# Test union
def test_union_1():
    set1 = PowerSet()
    set2 = PowerSet()
    for i in range(40000):
        set1.put(str(i))
        set2.put(str(i))
    assert set1.union(set2).size() == 40000


def test_union_2():
    set1 = PowerSet()
    set2 = PowerSet()
    for i in range(10000):
        set1.put(str(i))
    for i in range(5000, 15000):
        set2.put(str(i))
    assert set1.union(set2).size() == 15000


def test_union_3():
    set1 = PowerSet()
    set2 = PowerSet()
    assert set1.union(set2).size() == 0


# Test difference
def test_dif_1():
    set1 = PowerSet()
    set2 = PowerSet()
    assert set1.difference(set2).size() == 0


def test_dif_2():
    set1 = PowerSet()
    set2 = PowerSet()
    set1.put('1')
    assert set1.difference(set2).size() == 1


def test_dif_3():
    set1 = PowerSet()
    set2 = PowerSet()
    for i in range(10000):
        set1.put(str(i))
    for i in range(5000, 15000):
        set2.put(str(i))
    assert set1.difference(set2).size() == 5000


# Test issubset
def test_issubset_1():
    set1 = PowerSet()
    set2 = PowerSet()
    assert set1.issubset(set2) is True
    assert set2.issubset(set1) is True


def test_issubset_2():
    set1 = PowerSet()
    set2 = PowerSet()
    for i in range(10000):
        set1.put(str(i))
    for i in range(5000, 10000):
        set2.put(str(i))
    assert set1.issubset(set2) is True
