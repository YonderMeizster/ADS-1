from nativecahce import NativeCache
from random import randint

# Test put
def test_put_1():
    ncache = NativeCache()
    ncache.put('key', 1)
    assert ncache.get('key') == 1


def test_put_2():
    ncache = NativeCache()
    ncache.put('key', 1)
    key_ind = ncache.find('key')
    ncache.put('key1', 1)
    assert ncache.find('key') == key_ind


def test_put_3():
    ncache = NativeCache()
    ncache.put('key1', 1)
    key_ind = ncache.find('key')
    ncache.put('key2', 2)
    assert ncache.get('key1') == 1
    assert ncache.get('key2') == 2


def test_put_4():
    ncache = NativeCache()
    ncache.put('key', 1)
    ncache.put('key', 2)
    assert ncache.get('key') == 2


def test_put_5():
    ncache = NativeCache(1)
    ncache.put('key1', 1)
    assert ncache.get('key1') == 1


def test_put_6():
    ncache = NativeCache(1)
    ncache.put('key1', 1)
    ncache.put('key2', 1)
    ncache.put('key3', 1)
    ncache.put('key4', 1)
    assert ncache.get('key4') == 1
    assert ncache.keys() == ['key4']


def test_put_7():
    ncache = NativeCache(5)
    keys = ['key0', 'key1', 'key2', 'key3', 'key4']
    for index, key in enumerate(keys):
        ncache.put(key, index)

    for index, key in enumerate(keys):
        assert ncache.get(key) == index

    for hit in ncache.hits:
        assert hit == 1


def test_put_8():
    ncache = NativeCache(4)
    keys = ['key0', 'key1', 'key2', 'key3', 'key4']
    for index, key in enumerate(keys):
        ncache.put(key, index)

    for index in range(1, 5):
        assert ncache.get(keys[index]) == index

    assert ncache.get('key0') is None

    for hit in ncache.hits:
        assert hit == 1


def test_put_9():
    ncache = NativeCache(2)
    ncache.put('key1', 1)
    ncache.put('key2', 2)
    index_key1 = ncache.find('key1')
    ncache.hits[index_key1] += 1
    ncache.put('key3', 3)
    assert 'key1' in ncache.keys()
    assert 'key3' in ncache.keys()


def test_put_10():
    ncache = NativeCache(2)
    ncache.put('key1', 1)
    ncache.put('key2', 2)
    index_key2 = ncache.find('key2')
    ncache.hits[index_key2] += 1
    ncache.put('key3', 3)
    assert 'key2' in ncache.keys()
    assert 'key3' in ncache.keys()


def test_put_11():
    ncache = NativeCache()

    def find_same_hash(key):
        results = []
        i = int(key) + 1
        while len(results) < 3:
            if ncache.hash_fun(key) == ncache.hash_fun(str(i)):
                results.append(str(i))
            i += 1
        return results

    keys = find_same_hash('1')
    ncache.put('1', 1)
    for key in keys:
        ncache.put(key, 1)
    assert ncache.find(keys[2]) == 64


# Test find
def test_find_1():
    ncache = NativeCache()
    assert ncache.find('key') is None


def test_find_2():
    ncache = NativeCache()
    ncache.put('key', 1)
    assert isinstance(ncache.find('key'), int)


# Test get
def test_get_1():
    ncache = NativeCache(50)
    for i in range(50):
        ncache.put(str(i), i)

    for _ in range(100):
        for i in range(50):
            assert ncache.get(str(i)) == i

    for hit in ncache.hits:
        assert hit == 100


def test_get_2():
    ncache = NativeCache(1)
    assert ncache.get('key') is None


# Test clean_slot
def test_clean_slot_1():
    ncache = NativeCache(109)
    for i in range(109):
        ncache.put(i, i)
    for i in range(len(ncache.hits)):
        ncache.hits[i] = 2
    ncache.hits[0] = 1
    key = ncache.slots[0]
    assert key in ncache.keys()
    ncache.put('abrakadabra', 1)
    assert ncache.hits[0] == 0
    assert key not in ncache.keys()
