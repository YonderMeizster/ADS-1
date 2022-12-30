from stack import Stack


# Tests push
def test_push():
    s = Stack()
    s.push(5)
    assert s.size() == 1
    s.push(5)
    assert s.size() == 2


# Tests size
def test_size():
    s = Stack()
    assert s.size() == 0
    s.push(1)
    assert s.size() == 1
    s.pop()
    assert s.size() == 0


# Tests pop
def test_pop():
    s = Stack()
    assert s.pop() is None
    s.push(5)
    assert s.pop() == 5
    s.push(4)
    s.push(5)
    assert s.pop() == 5
    assert s.pop() == 4


# Tests peek
def test_peek():
    s = Stack()
    assert s.peek() is None
    s.push(1)
    assert s.peek() == 1
    assert s.size() == 1
