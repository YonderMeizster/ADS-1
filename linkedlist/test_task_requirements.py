import pytest
import sys
from io import StringIO
from linkedlist import LinkedList, Node


# Delete tests
def test_delete_empty():
    l = LinkedList()
    l.delete(1)
    assert l.head is l.tail is None


def test_delete_contain_one():
    l = LinkedList()
    l.add_in_tail(Node(1))
    l.delete(1)
    assert l.head is l.tail is None and l.len() == 0


def test_dont_delete_contain_one():
    l = LinkedList()
    l.add_in_tail(Node(1))
    l.delete(2)
    assert (l.head is l.tail and l.head.value == 1 and
            l.head.next is None)


def test_delete_head():
    l = LinkedList()
    for i in range(10):
        l.add_in_tail(Node(i))
    head_next = l.head.next
    l.delete(0)
    assert head_next is l.head


def test_delete_tail():
    l = LinkedList()
    nodes = [Node(1), Node(2), Node(3), Node(4), Node(5)]
    for node in nodes:
        l.add_in_tail(node)
    l.delete(5)
    assert l.tail is nodes[3]


def test_delete_head_and_tail():
    l = LinkedList()
    nodes = [Node(1), Node(2)]
    for node in nodes:
        l.add_in_tail(node)
    l.delete(1)
    l.delete(2)
    assert l.head is l.tail is None 


def test_delete_head_and_tail_more_elements():
    l = LinkedList()
    nodes = [Node(1), Node(2), Node(3), Node(4), Node(5)]
    for node in nodes:
        l.add_in_tail(node)
    l.delete(1)
    l.delete(5)
    assert l.head is nodes[1] and l.tail is nodes[3] and l.len() == 3


def test_delete_element_wich_equal_tail():
    """Delete element from body wich value is equal to tail's value.
    Tail shoudn't change"""
    l = LinkedList()
    nodes = [Node(1), Node(2), Node(5), Node(4), Node(5)]
    for node in nodes:
        l.add_in_tail(node)
    l.delete(5)
    assert nodes[1].next is nodes[3] and l.tail is nodes[4]


def test_delete_all_simple():
    l = LinkedList()
    for i in range(5):
        l.add_in_tail(Node(1))
    l.delete(1, True)
    assert l.head is l.tail is None


def test_delete_all_hard_1():
    nodes = [Node(5), Node(5), Node(3), Node(4), Node(5), Node(3),
             Node(5), Node(5)]
    l = LinkedList()
    for node in nodes:
        l.add_in_tail(node)
    l.delete(5, True)
    for i in range(len(nodes)):
        print(f'Is tail the Node{i}: {l.tail is nodes[i]}')

    assert l.head is nodes[2] and l.tail is nodes[5]


def test_delete_all_hard_2():
    nodes = [Node(5), Node(5), Node(3), Node(3), Node(3), Node(3), 
             Node(3), Node(3), Node(3), Node(5), Node(3), Node(5),
             Node(5)]
    l = LinkedList()
    for node in nodes:
        l.add_in_tail(node)
    l.delete(5, True)

    assert l.head is nodes[2] and l.tail is nodes[10]


def test_delete_all_hard_3():
    nodes = [Node(5), Node(5), Node(3), Node(3), Node(3), Node(3), 
             Node(3), Node(3), Node(3), Node(5), Node(3), Node(5),
             Node(5), Node(3), Node(3), Node(3), Node(3), Node(3),]
    l = LinkedList()
    for node in nodes:
        l.add_in_tail(node)
    l.delete(5, True)

    assert (l.head is nodes[2] and l.tail is nodes[len(nodes) - 1] and
           l.tail.next is None)


def test_delete_many_from_tail():
    nodes = [Node(5), Node(5), Node(3), Node(4), Node(5), Node(5),
             Node(5), Node(5)]
    l = LinkedList()
    for node in nodes:
        l.add_in_tail(node)
    l.delete(5, True)
    assert l.head is nodes[2] and l.tail is nodes[3] and l.tail.next is None


# Clean tests
def test_clean():
    l = LinkedList()
    l.add_in_tail(Node(1))
    l.add_in_tail(Node(1))
    l.add_in_tail(Node(1))
    l.clean()
    assert l.head is None and l.tail is None


def test_clean_second():
    l = LinkedList()
    reference_on_l = l
    l.clean()
    assert reference_on_l is l


# Find all tests
def test_find_all_in_empty():
    l = LinkedList()
    assert l.find_all(1) == []


def test_find_all_1_result():
    l = LinkedList()
    nodes = [Node(i) for i in range(125)]
    for node in nodes:
        l.add_in_tail(node)
    
    assert l.find_all(0)[0] is nodes[0]
    assert l.find_all(124)[0] is nodes[124]
    assert l.find_all(-1) == []


def test_find_all_multiple_results():
    l = LinkedList()
    node1 = Node(1)
    node2 = Node(1)
    node3 = Node(1)

    for i in range(10):
        l.add_in_tail(Node(2))
    l.add_in_tail(node1)
    for i in range(10):
        l.add_in_tail(Node(2))
    l.add_in_tail(node2)
    for i in range(10):
        l.add_in_tail(Node(2))
    l.add_in_tail(node3)

    results = l.find_all(1)

    assert (results[0] is node1 and results[1] is node2 and
            results[2] is node3)


# Lentgh tests
def test_empty_list_len():
    l = LinkedList()
    assert l.len() == 0


def test_add_first():
    l = LinkedList()
    node = Node(1)
    l.add_in_tail(node)

    assert l.len() == 1
    assert l.head is node is l.tail
    assert l.head.next is l.tail.next is None


# Insert test
def test_insert_one_element():
    l = LinkedList()
    node1 = Node(1)
    node2 = Node(2)
    l.add_in_tail(node1)
    l.insert(node1, node2)
    assert (l.head is node1 and l.tail is node2 and
            l.head.next is node2 and l.tail.next is None)


def test_insert_not_find():
    l = LinkedList()
    node1 = Node(1)
    node2 = Node(2)
    l.add_in_tail(node1)
    l.insert(Node(1), node2)
    assert l.head is l.tail and l.tail.next is None


def test_insert_empty_not_none():
    l = LinkedList()
    l.insert(Node(1), Node(2))


def test_insert_empty_with_none():
    l = LinkedList()
    node = Node(1)
    l.insert(None, node)
    assert l.head is l.tail is node and l.tail.next is None


def test_insert_node_with_next():
    l = LinkedList()
    nodes = [Node(1), Node(1), Node(1)]
    for node in nodes:
        l.add_in_tail(node)
    node = Node(1)
    l.insert(nodes[1], node)
    assert (l.head is nodes[0] and l.tail is nodes[2] and
            l.head.next.next is node and l.head.next.next.next is
            l.tail)
    

def test_insert_first():
    nodes = [Node(5), Node(5), Node(3), Node(4), Node(5), Node(3),
             Node(5), Node(5)]
    l = LinkedList()
    for node in nodes:
        l.add_in_tail(node)
    node1 = Node(4)
    l.insert(None, node1)
    assert l.head is node1 and l.head.next is nodes[0]