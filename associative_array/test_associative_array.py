from associative_array import NativeDictionary


# Test put
def test_put_1():
    as_ar = NativeDictionary(10)
    as_ar.put('1', 1)
    assert as_ar.get('stroka1') == 1


def test_put_2():
    as_pr = NativeDictionary(1)
    as_pr.put('', 1)
    assert as_pr.is_key('')
    assert as_pr.get('') == 1


def test_put_3():
    as_ar = NativeDictionary(3)
    as_ar.put('1', 1)
    as_ar.put('1', 2)
    assert as_ar.get('1') == 2

# Test is_key
def test_is_key():
    as_ar = NativeDictionary(3)
    as_ar.put('1', 1)
    as_ar.put('2', 2)
    as_ar.put('3', 3)

    assert as_ar.is_key('1') is True
    assert as_ar.is_key('2') is True
    assert as_ar.is_key('3') is True
    assert as_ar.is_key('4') is False
    assert as_ar.is_key('0') is False


# Test get
def test_is_key():
    as_ar = NativeDictionary(3)
    as_ar.put('1', 1)
    as_ar.put('2', 2)
    as_ar.put('3', 3)

    assert as_ar.get('1') == 1
    assert as_ar.get('2') == 2
    assert as_ar.get('3') == 3
    assert as_ar.get('4') is None
    assert as_ar.get('0') is None