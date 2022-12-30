import pytest
from doubly_linkedlist_cs106b import Node, LinkedList2_cs106b

# todo: adopt tests

# 2.1 Tests find
def test_find_in_empty():
    l = LinkedList2_cs106b()
    assert l.find(5) is None


def test_find_from_one():
    l = LinkedList2_cs106b()
    l.add_in_tail(Node(5))
    assert l.find(5) is l.head.next


def test_find_first():
    l = LinkedList2_cs106b()
    nodes = [Node(1), Node(1), Node(1), Node(1), Node(1), Node(1)]
    for node in nodes:
        l.add_in_tail(node)
    assert l.find(1) is nodes[0]
    assert l.head.next is nodes[0]


def test_find_normal():
    l = LinkedList2_cs106b()
    nodes = [Node(1), Node(2), Node(3), Node(3), Node(4), Node(5)]
    for node in nodes:
        l.add_in_tail(node)
    assert l.find(3) is nodes[2]
    #assert l.find(5) is nodes[5] is l.tail
    assert l.find(5) is nodes[5]


def test_find_missing():
    l = LinkedList2_cs106b()
    nodes = [Node(1), Node(2), Node(3)]
    for node in nodes:
        l.add_in_tail(node)
    assert l.find(5) is None


# 2.2 Tests find all
def test_find_all_empty():
    l = LinkedList2_cs106b()
    assert l.find_all(2) == []


def test_find_all_one():
    l = LinkedList2_cs106b()
    node = Node(1)
    l.add_in_tail(node)
    founded = l.find_all(1)
    assert founded == [node]
    assert l.head.next is founded[0]
    assert l.tail.prev is founded[0]
    #assert founded[0].next is None


def test_find_all_normal():
    l = LinkedList2_cs106b()
    nodes = [Node(1), Node(2), Node(2), Node(1), Node(2), Node(1)]
    for node in nodes:
        l.add_in_tail(node)
        founded = l.find_all(2)
    assert founded == [nodes[i] for i in (1, 2, 4)]
    assert founded[0] is l.head.next.next
    assert founded[-1] is l.tail.prev.prev


def test_find_all_from_all():
    l = LinkedList2_cs106b()
    nodes = [Node(1), Node(1), Node(1), Node(1), Node(1), Node(1)]
    for node in nodes:
        l.add_in_tail(node)
    founded = l.find_all(1)
    assert founded == nodes 
    assert founded[0] is l.head.next
    assert founded[-1] is l.tail.prev
    assert founded[-1].next is l.tail


# 2.3 Tests delete
def test_delete_empty():
    l = LinkedList2_cs106b()
    l.delete(1)
    assert l.head.next is l.tail
    assert l.tail.prev is l.head


def test_delete_one_element():
    l = LinkedList2_cs106b()
    l.add_in_tail(Node(1))
    l.delete(1)
    assert l.head.next is l.tail
    assert l.tail.prev is l.head


def test_delete_head():
    l = LinkedList2_cs106b()
    nodes = [Node(1), Node(2)]
    for node in nodes:
        l.add_in_tail(node)
    l.delete(1)
    assert l.head.next is nodes[1]
    assert l.tail.prev is nodes[1]


def test_delete_head_second():
    l = LinkedList2_cs106b()
    nodes = [Node(1), Node(2), Node(3)]
    for node in nodes:
        l.add_in_tail(node)
    l.delete(1)
    assert l.head.next is nodes[1]
    assert l.tail.prev is nodes[2]
    assert nodes[1].next is nodes[2]


def test_delete_tail():
    l = LinkedList2_cs106b()
    nodes = [Node(1), Node(2)]
    for node in nodes:
        l.add_in_tail(node)
    l.delete(2)
    assert l.head.next is l.tail.prev is nodes[0]
    assert nodes[0].prev is l.head
    assert nodes[0].next is l.tail


def test_delete_tail_second():
    l = LinkedList2_cs106b()
    nodes = [Node(1), Node(2), Node(3)]
    for node in nodes:
        l.add_in_tail(node)
    l.delete(3)
    assert l.head.next is nodes[0]
    assert l.tail.prev is nodes[1]
    assert l.head.prev is l.tail.next is None


def test_delete_first_encountered():
    l = LinkedList2_cs106b()
    nodes = [Node(1), Node(2), Node(3), Node(3)]
    for node in nodes:
        l.add_in_tail(node)
    l.delete(3)
    assert l.head.next is nodes[0]
    assert l.tail.prev is nodes[3]
    assert nodes[1].next is l.tail.prev


def test_delete_mid():
    l = LinkedList2_cs106b()
    nodes = [Node(1), Node(2), Node(3)]
    for node in nodes:
        l.add_in_tail(node)
    l.delete(2)
    assert l.head.next is nodes[0]
    assert l.tail.prev is nodes[2]
    assert l.head.prev is l.tail.next is None


# 2.4 Tests delete all
def test_deleteall_empty():
    l = LinkedList2_cs106b()
    l.delete(1, True)
    assert l.head.prev is l.tail.next is None
    assert l.head.next is l.tail
    assert l.tail.prev is l.head


def test_deleteall_one():
    l = LinkedList2_cs106b()
    l.add_in_head(Node(1))
    l.delete(1, True)
    assert l.head.prev is l.tail.next is None
    assert l.head.next is l.tail
    assert l.tail.prev is l.head


def test_deleteall_no_elements():
    l = LinkedList2_cs106b()
    nodes = [Node(1), Node(1), Node(1), Node(1), Node(1), Node(1)]
    for node in nodes:
        l.add_in_tail(node)
    l.delete(2, True)
    assert l.len() == 6
    assert l.head.next is nodes[0]
    assert l.tail.prev is nodes[-1]


def test_deleteall_head_and_tail():
    l = LinkedList2_cs106b()
    nodes = [Node(1), Node(1), Node(1), Node(2), Node(2), Node(1),
             Node(1), Node(1)]
    for node in nodes:
        l.add_in_tail(node)
    l.delete(1, True)
    assert l.head.next is nodes[3]
    assert l.tail.prev is nodes[4]
    assert l.tail.next is None
    assert l.head.prev is None


def test_deleteall():
    l = LinkedList2_cs106b()
    nodes = [Node(2), Node(1), Node(1), Node(2), Node(2), Node(2),
             Node(2), Node(1)]
    for node in nodes:
        l.add_in_tail(node)
    l.delete(2, True)
    assert l.head.next is nodes[1]
    assert l.tail.prev is nodes[-1]
    assert l.tail.next is None
    assert l.head.prev is None


def test_deleteall_long_head():
    l = LinkedList2_cs106b()
    nodes = [Node(2), Node(2), Node(2), Node(2), Node(2), Node(2),
             Node(1), Node(1)]
    for node in nodes:
        l.add_in_tail(node)
    l.delete(2, True)
    assert l.head.next is nodes[-2]
    assert l.tail.prev is nodes[-1]
    assert l.head.prev is l.tail.next is None
    assert l.head.next is nodes[-2]
    assert l.tail.prev is nodes[-1]


def test_deleteall_long_tail():
    l = LinkedList2_cs106b()
    nodes = [Node(2), Node(2), Node(1), Node(1), Node(1), Node(1),
             Node(1), Node(1)]
    for node in nodes:
        l.add_in_tail(node)
    l.delete(1, True)
    assert l.head.next is nodes[0]
    assert l.tail.prev is nodes[1]
    assert l.head.prev is l.tail.next is None


# 2.5 Tests insert
def test_insert_after_none_empty():
    l = LinkedList2_cs106b()
    node = Node(1)
    l.insert(None, node)
    assert l.head.next is l.tail.prev is node


def test_insert_after_none():
    l = LinkedList2_cs106b()
    nodes = [Node(1), Node(1), Node(1)]
    for node in nodes:
        l.add_in_tail(node)
    node = Node(1)
    l.insert(None, node)
    assert l.head.next is nodes[0]
    assert l.tail.prev is node
    assert nodes[-1].next is node
    assert node.prev is nodes[-1]
    assert node.next is l.tail


def test_insert_after_incorrect_empty():
    l = LinkedList2_cs106b()
    l.insert(Node(1), Node(1))
    assert l.head.next is l.tail
    assert l.tail.prev is l.head


def test_insert_after_incorrect():
    l = LinkedList2_cs106b()
    nodes = [Node(1), Node(1), Node(1)]
    for node in nodes:
        l.add_in_tail(node)
    node = Node(1)
    l.insert(Node(1), node)
    assert l.head.next is nodes[0]
    assert l.tail.prev is nodes[2]
    assert l.head.prev is l.tail.next is None


def test_insert_in_middle():
    l = LinkedList2_cs106b()
    nodes = [Node(1), Node(1), Node(1)]
    for node in nodes:
        l.add_in_tail(node)
    node = Node(1)
    l.insert(nodes[1], node)
    assert nodes[1].next is node
    assert node.prev is nodes[1]
    assert node.next is nodes[2]
    assert nodes[2].prev is node
    assert l.tail.prev is nodes[2]


def test_insert_in_tail():
    l = LinkedList2_cs106b()
    nodes = [Node(1), Node(1), Node(1)]
    for node in nodes:
        l.add_in_tail(node)
    node = Node(1)
    l.insert(nodes[2], node)
    assert l.tail.prev is node
    assert node.next is l.tail
    assert node.prev is nodes[2]
    assert nodes[2].next is node


# 2.6 Tests add_in_head
def test_addhead_empty():
    l = LinkedList2_cs106b()
    node = Node(1)
    l.add_in_head(node)
    assert l.head.next is node
    assert l.tail.prev is node
    assert node.prev is l.head
    assert node.next is l.tail
    assert l.head.prev is None
    assert l.tail.next is None


def test_addhead_normal():
    l = LinkedList2_cs106b()
    nodes = [Node(1), Node(1), Node(1), Node(1), Node(1), Node(1)]
    for node in nodes:
        l.add_in_head(node)

    assert l.head.next is nodes[-1]
    assert l.tail.prev is nodes[0]
    assert nodes[-1].next is nodes[-2]
    assert nodes[0].next is l.tail
    assert l.head.prev is None
    assert l.tail.next is None


# 2.7 Tests clean
def test_clean_empty():
    l = LinkedList2_cs106b()
    l.clean()
    assert l.head.next is l.tail
    assert l.tail.prev is l.head
    assert l.head.prev is None
    assert l.tail.next is None


def test_clean_normal():
    l = LinkedList2_cs106b()
    nodes = [Node(1), Node(2), Node(3)]
    for node in nodes:
        l.add_in_tail(node)
    l.clean()
    assert l.head.next is l.tail
    assert l.tail.prev is l.head
    assert l.head.prev is None
    assert l.tail.next is None


# 2.8 Tests len
def test_len_empty():
    l = LinkedList2_cs106b()
    assert l.len() == 0


def test_len_one_len():
    l = LinkedList2_cs106b()
    l.add_in_tail(Node(1))
    assert l.len() == 1


def test_len_normal():
    l = LinkedList2_cs106b()
    for i in range(100):
        l.add_in_tail(Node(1))
    assert l.len() == 100


def test_len_with_delete():
    l = LinkedList2_cs106b()
    for i in range(50):
        l.add_in_tail(Node(1))
        l.add_in_tail(Node(2))
    l.delete(1)
    assert l.len() == 99
