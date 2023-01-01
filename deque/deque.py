class Deque:
    def __init__(self):
        self.deque = []

    def addFront(self, item):
        self.deque = [item] + self.deque

    def addTail(self, item):
        self.deque.append(item)

    def removeFront(self):
        try:
            return self.deque.pop(0)
        except IndexError:
            return None

    def removeTail(self):
        try:
            return self.deque.pop(-1)
        except IndexError:
            return None

    def size(self):
        return len(self.deque)
