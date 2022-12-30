from stack import Stack


def verify_parentheses(parentheses: str):
    s = Stack()
    for parenthesis in parentheses:
        if bracket == '(':
            s.push(bracket)
            continue
        if s.pop() == None:
            return False
    return s.size() == 0
