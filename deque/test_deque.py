from deque import Deque


# Test size
def test_deque_size_empty():
    deque = Deque()
    assert deque.size() == 0


def test_deque_size_add_front():
    deque = Deque()
    assert deque.size() == 0
    deque.addFront(1)
    assert deque.size() == 1


def test_deque_size_add_tail():
    deque = Deque()
    assert deque.size() == 0
    deque.addTail(1)
    assert deque.size() == 1


def test_deque_size_add_both():
    deque = Deque()
    assert deque.size() == 0
    deque.addFront(1)
    deque.addTail(1)
    assert deque.size() == 2


# Test add tail and remove tail
def test_removeTail_empty():
    deque = Deque()
    assert deque.removeTail() is None


def test_addTail_removeTail():
    deque = Deque()
    for i in range(1000):
        deque.addTail(i)
    assert deque.size() == 1000
    for i in range(999, -1, -1):
        assert deque.removeTail() == i
        assert deque.size() == i


# Test add front and remove front
def test_removeFront_empty():
    deque = Deque()
    assert deque.removeFront() is None


def test_addFront_removeFront():
    deque = Deque()
    for i in range(1000):
        deque.addFront(i)
    assert deque.size() == 1000
    for i in range(999, -1, -1):
        assert deque.removeFront() == i
        assert deque.size() == i


# Test add front and remove tail
def test_addFront_removeTail():
    deque = Deque()
    for i in range(1000):
        deque.addFront(i)
    for i in range(1000):
        assert deque.removeTail() == i


# Test add tail and remove front
def test_addTail_removeFront():
    deque = Deque()
    for i in range(1000):
        deque.addTail(i)
    for i in range(1000):
        assert deque.removeFront() == i