from linkedlist import Node
from linkedlist import LinkedList


def sum_linkedlists(first : LinkedList, second : LinkedList):
    """Return linked list in which every element is the sum of the
    elements from first and second. first and second must to be the same
    length if it not returns None. If first and second are empty,
    returns empty new linkedlist
    
    Values of Nodes in linked list have to support sum operation.
    Function use '+' operator"""
    if first == None or second == None:
        # I would prefer to raise an exception in this case, but
        # so be it
        return None

    summed_values = LinkedList()
    curr_in_first = first.head
    curr_in_second = second.head
    
    while curr_in_first != None or curr_in_second != None:
        #It is possible to check immediately if the lengths of the lists
        # are equal via their .len() method, but this implementation
        # speeds up execution by 10%
        if ((curr_in_first.next == None or
             curr_in_second.next == None) and
             curr_in_first.next != curr_in_second.next): return None
        summed_values.add_in_tail(Node(curr_in_first.value + 
                                       curr_in_second.value))
        curr_in_first = curr_in_first.next
        curr_in_second = curr_in_second.next

    return summed_values
