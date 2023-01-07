class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class OrderedList:
    def __init__(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def _isempty(self):
        if not self.head:
            return True
        return False

    def _tricky(self):
        return 1 if self.__ascending else -1

    def compare(self, v1, v2):
        if v1 > v2:
            return 1 
        if v1 < v2:
            return -1
        return 0

    def add(self, value):
        node = Node(value)
        if self._isempty():
            self.head = self.tail = node
            return
        curr = self.head
        while curr:
            if self.compare(node.value, curr.value) * self._tricky() < 1:
                node.next = curr
                node.prev = curr.prev
                curr.prev = node
                if self.head is curr:
                    self.head = node
                    return
                node.prev.next = node
                return
            curr = curr.next
        self.tail.next = node
        node.prev = self.tail
        self.tail = node

    def find(self, val):
        if self._isempty():
            return
        curr = self.head
        while curr:
            if self.compare(val, curr.value) == 0:
                return curr
            if self.compare(val, curr.value) * self._tricky() == -1:
                return
            curr = curr.next

    def delete(self, val):
        node = self.find(val)
        if not node: return None

        if self.head is self.tail:
            self.clean(asc = self.__ascending)
            return
        
        if self.head is node:
            self.head.next.prev = None
            self.head = self.head.next
            return
        if self.tail is node:
            self.tail.prev.next = None
            self.tail = self.tail.prev
            return

        node.next.prev = node.prev
        node.prev.next = node.next
        node.next = node.prev = None

    def clean(self, asc):
        self.__init__(asc)

    def len(self):
        count = 0
        curr = self.head
        while curr:
            count += 1
            curr = curr.next
        return count

    def get_all(self):
        r = []
        node = self.head
        while node != None:
            r.append(node)
            node = node.next
        return r

    def _get_all_debug(self):
        list1 = []
        curr = self.head
        while curr:
            list1.append(curr.value)
            curr = curr.next
        return list1 

class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1 : str, v2 : str) -> int:
        v1 = v1.rstrip()
        v2 = v2.rstrip()
        if v1 > v2:
            return 1
        if v1 < v2:
            return -1
        return 0
