from stack import Stack


def verify_parentheses(parentheses: str):
    s = Stack()
    for parenthesis in parentheses:
        if parenthesis == '(':
            s.push(parenthesis)
            continue
        if s.pop() == None:
            return False
    return s.size() == 0
