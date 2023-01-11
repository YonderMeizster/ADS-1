from powerset import PowerSet
import time
import random
import string


# start = time.time()
# for i in range(20):
#     pwset.put('value')
# end = time.time()
# print('Время выполнения: {:.3f}'.format(end - start))


# Test put
def test_put_1():
    pwset = PowerSet()
    pwset.put('1')
    assert pwset._get_all() == ['1']


def test_put_2():
    pwset = PowerSet()

    start = time.time()
    for i in range(200000):
        pwset.put(str(i))
    end = time.time()
    print(f'Время добавления = {end - start}')
    start = time.time()
    size = pwset.size()
    end = time.time()
    assert size == 200000
    print(f'Время вычисления числа значений = {end - start}')
    start = time.time()
    length = len(pwset.slots)
    end = time.time()
    print(f'Время вычисления числа слотов = {end - start}')

    print(f'Число элементов = {size}, а слотов = {length}')


def test_put_dublicates():
    pwset = PowerSet()
    pwset.put('1')
    assert pwset.get('1')
    pwset.put('1')    
    assert pwset.size() == 1


test_put_2()