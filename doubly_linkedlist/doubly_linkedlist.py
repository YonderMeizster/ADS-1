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
        while node is not None:
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
        while node is not None:
            if node.value == val:
                founded.append(node)
            node = node.next
        return founded

    def delete(self, val, all=False):
        if self.head is self.tail is None: return
        
        if not all:
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
            while self.head.value == val:
                if self.head is self.tail:
                    self.head = self.tail = None
                    return
                self.head = self.head.next
                self.head.prev = None
            curr_node = self.head.next
            prev_node = self.head
            prev_node.next = None
            self.tail = prev_node
            while curr_node != None:
                if curr_node.value != val:
                    prev_node.next = curr_node
                    curr_node.prev = prev_node
                    prev_node = curr_node
                    self.tail = curr_node
                curr_node = curr_node.next
                prev_node.next = None

    def clean(self):
        self.head = self.tail = None

    def len(self):
        length = 0
        node = self.head
        while node is not None:
            length += 1
            node = node.next
        return length

    def insert(self, afterNode, newNode):
        newNode.next = newNode.prev = None
        if afterNode is None:
            if self.head is self.tail is None:
                self.head = self.tail = newNode
            else:
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode
        else:
            curr_node = self.head
            while curr_node is not None:
                if curr_node is afterNode:
                    break
                curr_node = curr_node.next
            else:
                return
            if afterNode is self.tail:
                self.tail = newNode
            else:
                afterNode.next.prev = newNode
                newNode.next = afterNode.next
            afterNode.next = newNode
            newNode.prev = afterNode

    def add_in_head(self, newNode):
        newNode.next = newNode.prev = None
        if self.head is None:
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
        self.head = newNode
