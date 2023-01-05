from stack import Stack


def estimate(stack, operation):
    operand1 = stack.pop()
    operand2 = stack.pop()
    return eval(f'{operand1} {operation} {operand2}')


def calculate(expression: Stack):
    operators = {'+': lambda s: s.push(estimate(s, '+')),
                 '-': lambda s: s.push(estimate(s, '-')),
                 '*': lambda s: s.push(estimate(s, '*')),
                 '/': lambda s: s.push(estimate(s, '/')),
                 '=': lambda s: s.pop()}
    digits = Stack()
    answer = None
    while expression.size() > 0:
        symbol = str(expression.pop())
        if symbol.isdigit():
            digits.push(int(symbol))
            continue
        answer = operators[symbol](digits)
    return answer
