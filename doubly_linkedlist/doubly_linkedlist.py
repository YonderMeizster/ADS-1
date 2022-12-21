class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class LinkedList2:  
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def find(self, val):
        if self.head:
            node = self.head
        else:
            return None
        while node != None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        founded = []
        if self.head:
            node = self.head
        else:
            return founded
        while node != None:
            if node.value == val:
                founded.append(node)
            node = node.next
        return founded

    def delete(self, val, all=False):
        #todo: add all=True case
        if all == False:
            node = self.find(val)
            if not node: return None
            if self.head is node:
                if self.tail is node:
                    self.head = self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = None
            elif self.tail is node:
                self.tail = self.tail.prev
                self.tail.next = None
            else:
                node.prev.next = node.next
                node.next.prev = node.prev
        else:
            pass


    def clean(self):
        self.head = self.tail = None

    def len(self):
        length = 0
        node = self.head
        while node != None:
            length += 1
            node = node.next
        return length

    def insert(self, afterNode, newNode):
        pass # здесь будет ваш код

    def add_in_head(self, newNode):
        if self.head is None:
            self.head = self.tail = newNode
            newNode.prev = newNode.next = None
        else:
            newNode.next = self.head
            self.head = newNode