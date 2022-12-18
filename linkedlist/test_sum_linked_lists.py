import pytest
from sum_linked_lists import sum_linkedlists
from linkedlist import LinkedList, Node

def test_empties():
    l1 = LinkedList()
    l2 = LinkedList()
    sum_of_lists = sum_linkedlists(l1, l2)
    assert (isinstance(sum_of_lists, LinkedList) and
           sum_of_lists.len() == 0)
    

def test_normal_case():
    l1 = LinkedList()
    l2 = LinkedList()
    nodes = [Node(1), Node(2), Node(3), Node(4), Node(5)]
    for node in nodes:
        l1.add_in_tail(Node(1))
        l2.add_in_tail(node)
    summed = sum_linkedlists(l1, l2)
    current_node = summed.head
    index = 0
    while current_node != None:
        assert current_node.value == nodes[index].value + 1
        current_node = current_node.next
        index += 1


def test_one_shorter():
    l1 = LinkedList()
    l2 = LinkedList()
    nodes = [Node(1), Node(2), Node(3), Node(4), Node(5)]
    for node in nodes:
        l1.add_in_tail(Node(1))
        l2.add_in_tail(node)
    l2.add_in_tail(Node(1))
    assert sum_linkedlists(l1, l2) == None
