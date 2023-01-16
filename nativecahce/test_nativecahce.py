from nativecahce import NativeCache


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
    ncache.put()
    
    

# Test find
def test_find_1():
    pass


# ncache = NativeCache(sz = 5)
# ncache.put('key', 1)
# ncache.put('key1', 1)
# ncache.put('key2', 1)
# ncache.put('key3', 1)
# ncache.put('key4', 1)
# ncache.put('key', 1)
# print(ncache.get('key'))
# print(ncache.get('key'))
# print(ncache.get('key'))
# print(ncache)
