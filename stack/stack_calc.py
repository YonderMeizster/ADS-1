from stack import Stack


def calculate(expression : Stack):
    operators = {'+' : lambda s: s.push(s. pop() + s.pop()),
                 '-' : lambda s: s.push(s.pop() - s.pop()),
                 '*' : lambda s: s.push(s.pop() * s.pop()),
                 '/' : lambda s: s.push(s.pop() / s.pop()),
                 '=' : lambda s: s.pop()}
    digits = Stack()
    answer = None
    while expression.size() > 0:
        symbol = str(expression.pop())
        if symbol.isdigit():
            digits.push(int(symbol))
            continue
        answer = operators[symbol](digits)
    return answer
