import pytest
from doubly_linkedlist import LinkedList2, Node


# 2.1 Tests find
def test_find_in_empty():
    l = LinkedList2()
    assert l.find(5) is None


def test_find_from_one():
    l = LinkedList2()
    l.add_in_tail(Node(5))
    assert l.find(5) is l.tail


def test_find_first():
    l = LinkedList2()
    nodes = [Node(1), Node(1), Node(1), Node(1), Node(1), Node(1)]
    for node in nodes:
        l.add_in_tail(node)
    assert l.find(1) is nodes[0]
    assert l.head.next is nodes[1]


def test_find_normal():
    l = LinkedList2()
    nodes = [Node(1), Node(2), Node(3), Node(3), Node(4), Node(5)]
    for node in nodes:
        l.add_in_tail(node)
    assert l.find(3) is nodes[2]
    assert l.find(5) is nodes[5] is l.tail
    assert l.find(5).next is None


def test_find_missing():
    l = LinkedList2()
    nodes = [Node(1), Node(2), Node(3)]
    for node in nodes:
        l.add_in_tail(node)
    assert l.find(5) is None


# 2.2 Tests find all
def test_find_all_empty():
    l = LinkedList2()
    assert l.find_all(2) == []


def test_find_all_one():
    l = LinkedList2()
    node = Node(1)
    l.add_in_tail(node)
    founded = l.find_all(1)
    assert (founded == [node] and l.head is founded[0] and
            l.tail is founded[0] and founded[0].next is None)


def test_find_all_normal():
    l = LinkedList2()
    nodes = [Node(1), Node(2), Node(2), Node(1), Node(2), Node(1)]
    for node in nodes:
        l.add_in_tail(node)
        founded = l.find_all(2)
    assert (founded == [nodes[i] for i in (1, 2, 4)] and
            founded[0] is l.head.next and founded[-1] is l.tail.prev)


def test_find_all_in_two_lists():
    l1 = LinkedList2()
    l2 = LinkedList2()
    for i in range(10):
        l1.add_in_tail(Node(1))
        l2.add_in_tail(Node(1))
    founded2 = l2.find_all(1)
    l1.tail.next = l2.head
    l2.head.prev = l1.tail
    l1.tail = l2.tail
    founded1 = l1.find_all(1)
    assert founded1[0] is l1.head and founded1[-1] is l2.tail
    assert founded2[0] is l2.head and founded2[-1] is l2.tail


def test_find_all_from_all():
    l = LinkedList2()
    nodes = [Node(1), Node(1), Node(1), Node(1), Node(1), Node(1)]
    for node in nodes:
        l.add_in_tail(node)
    founded = l.find_all(1)
    assert (founded == nodes and founded[0] is l.head and
            founded[-1] is l.tail and founded[-1].next is None)


# 2.3 Tests delete
def test_delete_empty():
    l = LinkedList2()
    l.delete(1)
    assert l.head is l.tail is None


def test_delete_one_element():
    l = LinkedList2()
    l.add_in_tail(Node(1))
    l.delete(1)
    assert l.head is l.tail is None


def test_delete_head():
    l = LinkedList2()
    nodes = [Node(1), Node(2)]
    for node in nodes:
        l.add_in_tail(node)
    l.delete(1)
    assert (l.head is nodes[1] and l.tail is nodes[1] and
            l.head.next is l.head.prev is l.tail.next is
            l.tail.prev is None)


def test_delete_head_second():
    l = LinkedList2()
    nodes = [Node(1), Node(2), Node(3)]
    for node in nodes:
        l.add_in_tail(node)
    l.delete(1)
    assert (l.head is nodes[1] and l.tail is nodes[2] and
            l.head.next == l.tail and l.tail.prev == l.head and
            l.head.prev is l.tail.next is None)


def test_delete_tail():
    l = LinkedList2()
    nodes = [Node(1), Node(2)]
    for node in nodes:
        l.add_in_tail(node)
    l.delete(2)
    assert (l.head is nodes[0] and l.tail is nodes[0] and
            l.head.next is l.head.prev is l.tail.next is
            l.tail.prev is None)


def test_delete_tail_second():
    l = LinkedList2()
    nodes = [Node(1), Node(2), Node(3)]
    for node in nodes:
        l.add_in_tail(node)
    l.delete(3)
    assert (l.head is nodes[0] and l.tail is nodes[1] and
            l.head.next == l.tail and l.tail.prev == l.head and
            l.head.prev is l.tail.next is None)


def test_delete_first_encountered():
    l = LinkedList2()
    nodes = [Node(1), Node(2), Node(3), Node(3)]
    for node in nodes:
        l.add_in_tail(node)
    l.delete(3)
    assert (l.head is nodes[0] and l.tail is nodes[3] and
            l.head.next is nodes[1] and nodes[1].next is
            l.tail and l.tail.prev is nodes[1])


def test_delete_mid():
    l = LinkedList2()
    nodes = [Node(1), Node(2), Node(3)]
    for node in nodes:
        l.add_in_tail(node)
    l.delete(2)
    assert (l.head is nodes[0] and l.tail is nodes[2] and
            l.head.next == l.tail and l.tail.prev == l.head and
            l.head.prev is l.tail.next is None)


# 2.4 Tests delete all
def test_deleteall_empty():
    l = LinkedList2()
    l.delete(1, True)
    assert l.head is l.tail is None


def test_deleteall_one():
    l = LinkedList2()
    l.add_in_head(Node(1))
    l.delete(1, True)
    assert l.head is l.tail is None


def test_deleteall_no_elements():
    l = LinkedList2()
    nodes = [Node(1), Node(1), Node(1), Node(1), Node(1), Node(1)]
    for node in nodes:
        l.add_in_tail(node)
    l.delete(2, True)
    assert l.len() == 6
    assert l.head is nodes[0]
    assert l.tail is nodes[-1]


def test_deleteall_head_and_tail():
    l = LinkedList2()
    nodes = [Node(1), Node(1), Node(1), Node(2), Node(2), Node(1),
             Node(1), Node(1)]
    for node in nodes:
        l.add_in_tail(node)
    l.delete(1, True)
    assert l.head is nodes[3]
    assert l.tail is nodes[4]
    assert l.tail.next is None
    assert l.head.prev is None


def test_deleteall():
    l = LinkedList2()
    nodes = [Node(2), Node(1), Node(1), Node(2), Node(2), Node(2),
             Node(2), Node(1)]
    for node in nodes:
        l.add_in_tail(node)
    l.delete(2, True)
    assert l.head is nodes[1]
    assert l.tail is nodes[-1]
    assert l.tail.next is None
    assert l.head.prev is None


def test_deleteall_long_head():
    l = LinkedList2()
    nodes = [Node(2), Node(2), Node(2), Node(2), Node(2), Node(2),
             Node(1), Node(1)]
    for node in nodes:
        l.add_in_tail(node)
    l.delete(2, True)
    assert l.head is nodes[-2]
    assert l.tail is nodes[-1]
    assert l.head.prev is l.tail.next is None
    assert l.head.next is l.tail
    assert l.tail.prev is l.head


def test_deleteall_long_tail():
    l = LinkedList2()
    nodes = [Node(2), Node(2), Node(1), Node(1), Node(1), Node(1),
             Node(1), Node(1)]
    for node in nodes:
        l.add_in_tail(node)
    l.delete(1, True)
    assert l.head is nodes[0]
    assert l.tail is nodes[1]
    assert l.head.prev is l.tail.next is None
    assert l.head.next is l.tail
    assert l.tail.prev is l.head


# 2.5 Tests insert
def test_insert_after_none_empty():
    l = LinkedList2()
    node = Node(1)
    l.insert(None, node)
    assert l.head is l.tail is node
    assert node.next is node.prev is None


def test_insert_after_none():
    l = LinkedList2()
    nodes = [Node(1), Node(1), Node(1)]
    for node in nodes:
        l.add_in_tail(node)
    node = Node(1)
    l.insert(None, node)
    assert l.head is nodes[0]
    assert l.tail is node
    assert nodes[-1].next is node
    assert node.prev is nodes[-1]
    assert node.next is None


def test_insert_after_incorrect_empty():
    l = LinkedList2()
    l.insert(Node(1), Node(1))
    assert l.head is l.tail is None


def test_insert_after_incorrect():
    l = LinkedList2()
    nodes = [Node(1), Node(1), Node(1)]
    for node in nodes:
        l.add_in_tail(node)
    node = Node(1)
    l.insert(Node(1), node)
    assert l.head is nodes[0]
    assert l.tail is nodes[2]
    assert l.head.next is nodes[1]
    assert l.head.next.next is nodes[2]
    assert l.head.prev is l.tail.next is None


def test_insert_in_middle():
    l = LinkedList2()
    nodes = [Node(1), Node(1), Node(1)]
    for node in nodes:
        l.add_in_tail(node)
    node = Node(1)
    l.insert(nodes[1], node)
    assert nodes[1].next is node
    assert node.prev is nodes[1]
    assert node.next is nodes[2]
    assert nodes[2].prev is node
    assert l.tail is nodes[2]


def test_insert_in_tail():
    l = LinkedList2()
    nodes = [Node(1), Node(1), Node(1)]
    for node in nodes:
        l.add_in_tail(node)
    node = Node(1)
    l.insert(nodes[2], node)
    assert l.tail is node
    assert node.next is None
    assert node.prev is nodes[2]
    assert nodes[2].next is node


# 2.6 Tests add_in_head
def test_addhead_empty():
    l = LinkedList2()
    node = Node(1)
    l.add_in_head(node)
    assert (l.head is l.tail is node and l.head.prev is l.head.next is
            l.tail.prev is l.tail.next is None)


def test_addhead_normal():
    l = LinkedList2()
    nodes = [Node(1), Node(1), Node(1), Node(1), Node(1), Node(1)]
    for node in nodes:
        l.add_in_head(node)

    assert l.head is nodes[-1]
    assert l.tail is nodes[0]
    assert l.head.prev is None
    assert l.tail.next is None
    assert l.head.next is nodes[-2]
    assert l.tail.prev is nodes[1]


# 2.7 Tests clean
def test_clean_empty():
    l = LinkedList2()
    l.clean()
    assert l.head is l.tail is None


def test_clean_normal():
    l = LinkedList2()
    nodes = [Node(1), Node(2), Node(3)]
    for node in nodes:
        l.add_in_tail(node)
    l.clean()
    assert l.head is l.tail is None


# 2.8 Tests len
def test_len_empty():
    l = LinkedList2()
    assert l.len() == 0


def test_len_one_len():
    l = LinkedList2()
    l.add_in_tail(Node(1))
    assert l.len() == 1


def test_len_normal():
    l = LinkedList2()
    for i in range(100):
        l.add_in_tail(Node(1))
    assert l.len() == 100


def test_len_with_delete():
    l = LinkedList2()
    for i in range(50):
        l.add_in_tail(Node(1))
        l.add_in_tail(Node(2))
    l.delete(1)
    assert l.len() == 99
