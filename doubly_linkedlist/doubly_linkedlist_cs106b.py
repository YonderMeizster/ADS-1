from doubly_linkedlist import Node, LinkedList2

class _Fiction_node():
    def __init__(self):
        self.next = None
        self.prev = None


class LinkedList2_cs106b(LinkedList2):
    """Additiinal task. Doubly linked list realization with dummy
    nodes"""
    def __init__(self):
        self.head = _Fiction_node()
        self.tail = _Fiction_node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_in_tail(self, item):
        item.prev = self.tail.prev
        item.prev.next = item
        self.tail.prev = item
        item.next = self.tail

    def add_in_head(self, item):
        item.next = self.head.next
        item.next.prev = item
        self.head.next = item
        item.prev = self.head

    def clean(self):
        self = self.__init__()

    def len(self):
        curr = self.head.next
        count = 0
        while isinstance(curr, Node):
            count += 1
            curr = curr.next
        return count

    def find(self, val):
        curr = self.head.next
        while isinstance(curr, Node):
            if curr.value == val:
                return curr
            curr = curr.next
        return None

    def _contains_node(self, node):
        curr = self.head.next
        while isinstance(curr, Node):
            if curr is node:
                return True
            curr = curr.next
        return False

    def find_all(self, val):
        founded = []
        curr = self.head.next
        while isinstance(curr, Node):
            if curr.value == val:
                founded.append(curr)
            curr = curr.next
        return founded

    def delete(self, val, all=False):
        curr = self.head.next
        while isinstance(curr, Node):
            if curr.value == val:
                curr.prev.next = curr.next
                curr.next.prev = curr.prev
                if not all: break
            curr = curr.next
    
    def insert(self, afterNode, newNode):
        if afterNode is None:
            if not isinstance(self.head.next, Node):
                self.add_in_head(newNode)
                return
            self.add_in_tail(newNode)
            return
        if not self._contains_node(afterNode) : return
        newNode.next = afterNode.next
        newNode.prev = afterNode
        afterNode.next = newNode
        newNode.next.prev = newNode
        
