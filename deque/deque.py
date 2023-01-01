class Deque:
    def __init__(self):
        self.deque = []

    def addFront(self, item):
        self.deque = [item] + self.deque

    def addTail(self, item):
        self.deque.append(item)

    def removeFront(self):
        if self.size() > 0:
            return self.deque.pop(0)
        return None

    def removeTail(self):
        if self.size() > 0:
            return self.deque.pop(-1)
        return None

    def size(self):
        return len(self.deque)
