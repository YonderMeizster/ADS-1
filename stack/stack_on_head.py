from stack import Stack


class StackOnListHead(Stack):
    """This is additional class. This implementation works with list's
    start instead of its end."""
    def pop(self):
        try:
            return self.stack.pop(0)
        except IndexError:
            return None

    def push(self, value):
        temp = [value]
        temp.extend(self.stack)
        self.stack = temp
        

    def peek(self):
        try:
            return self.stack[0]
        except IndexError:
            return None
