from nativecahce import NativeCache


# Test put
def test_put_1():
    ncache = NativeCache()
    ncache.put('key', 1)
    assert isinstance(ncache.find('key'), int)

def test_put_1():
    ncache = NativeCache()
    ncache.put('key', 1)
    key_ind = ncache.find('key')
    ncache.put('key1', 1)
    assert ncache.find('key') == key_ind

def test_put_2():
    ncache = NativeCache()
    ncache.put('key', 1)
    key_ind = ncache.find('key')
    ncache.put('key', 2)
    assert ncache.find('key') == key_ind

def test_put_3():
    ncache = NativeCache()
    ncache.put('key', 1)
    ncache.put('key', 2)
    assert ncache.get('key') == 2

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