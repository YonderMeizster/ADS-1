from asd1_queue import Queue


# Tests size
def test_size():
    queue = Queue()
    assert queue.size() == 0


# Tests enque
def test_enque():
    queue = Queue()
    queue.enqueue(1)
    assert queue.size() == 1
    queue.enqueue(1)
    assert queue.size() == 2


# Tests dequeue
def test_dequeue_1():
    queue = Queue()
    queue.enqueue(1)
    result = queue.dequeue()
    assert result == 1
    assert queue.size() == 0


def test_dequeue_2():
    queue = Queue()
    for i in range(1000):
        queue.enqueue(i)
    assert queue.size() == 1000
    for i in range(1000):
        assert queue.dequeue() == i
    assert queue.size() == 0


def test_dequeue_empty():
    queue = Queue()
    assert queue.dequeue() is None
