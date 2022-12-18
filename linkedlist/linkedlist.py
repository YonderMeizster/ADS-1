class Node:

    def __init__(self, v):
        self.value = v
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def _find_ref(self, node):
        curr = self.head
        while curr != None:
            if curr is node:
                return curr
            curr = curr.next
        raise ValueError('no such element')

    def find_all(self, val):
        result = []
        node = self.head

        while node != None:
            if node.value == val:
                result.append(node)
            node = node.next

        return result

    def delete(self, val, all=False):
        if self.head == None:
            return
        
        if all == True:
            while self.head != None and self.head.value == val:
                self.head = self.head.next
            if self.head == None:
                self.tail = None
                return
            
            prev = self.head
            curr = self.head.next
            while curr != None:
                if curr.value == val:
                    if self.tail is curr:
                        self.tail = prev
                        break
                else:
                    prev.next = curr
                    prev = curr
                curr = curr.next
        else:
            if self.head.value == val:
                self.head = self.head.next
                if self.head == None:
                    self.tail = None
            else:
                prev = self.head
                curr = self.head.next
                while curr != None:
                    if curr.value == val:
                        prev.next = curr.next
                        if self.tail is curr:
                            self.tail = prev
                        break
                    prev = prev.next
                    curr = curr.next

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
        newNode.next = None
        if afterNode == None:
            if self.head is self.tail:
                if self.head == None:
                    self.head = self.tail = newNode
            else:
                newNode.next = self.head
                self.head = newNode
        else:
            try:
                curr = self._find_ref(afterNode)
                if curr is self.tail:
                    self.tail = newNode
                newNode.next = curr.next
                curr.next = newNode
            except: return
