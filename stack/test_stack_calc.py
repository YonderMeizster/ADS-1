from stack_calc import calculate
from stack import Stack


def test_calc_1():
    test_stack = Stack()
    test_stack.push('=')
    test_stack.push('+')
    test_stack.push(9)
    test_stack.push('*')
    test_stack.push(5)
    test_stack.push('+')
    test_stack.push(2)
    test_stack.push(8)

    assert calculate(test_stack) == 59


def test_calc_2():
    test_stack = Stack()
    test_stack.push('+')
    test_stack.push(9)
    test_stack.push('*')
    test_stack.push(5)
    test_stack.push('+')
    test_stack.push(2)
    test_stack.push(8)

    assert calculate(test_stack) is None
