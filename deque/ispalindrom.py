from deque import Deque


def ispalindrom(input: str):
    deque = Deque()
    for char in input:
        deque.addTail(char)
    for char in input:
        if deque.removeTail() != char:
            return False
    return True
