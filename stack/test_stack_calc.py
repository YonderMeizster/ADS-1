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


def test_calc_3():
    test_stack = Stack()
    test_stack.push('=')
    test_stack.push('-')
    test_stack.push(20)
    test_stack.push(6)

    assert calculate(test_stack) == 14


def test_calc_4():
    test_stack = Stack()
    test_stack.push('=')
    test_stack.push('/')
    test_stack.push(4)
    test_stack.push(2)

    assert calculate(test_stack) == 2.0