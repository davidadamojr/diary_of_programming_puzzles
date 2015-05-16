"""
How would you design a stack which, in addition to push and pop, also has a function
min which returns the minimum element? Push, pop and min should all operate in
O(1) time.
"""

class Stack(object):
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def min(self):
        return self.min_stack[-1]

    def push(self, value):
        if value <= self.min():
            self.min_stack.append(value)

        self.stack.append(value)

    def pop(self):
        if value == self.min():
            self.min_stack.pop()

        return self.stack.pop()

    def peek(self):
        return self.stack[-1]