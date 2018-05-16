"""
Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
Therefore, in real life, we would likely start a new stack when the previous stack 
exceeds some threshold. Implement a data structure "SetOfStacks" that mimics this.
"SetOfStacks" a should be composed of several stacks and should create a new stack 
once the previous one exceeds capacity. "SetOfStacks.push()" and "SetOfStacks.pop()" 
should have behave identically to a single stack (that is pop() should return the 
same values as it would if there were just a single stack).

FOLLOW UP

Implement a function "popAt(int index)" which performs a pop operation on a specific 
substack.
"""


class Stack:
    def __init__(self, capacity):
        self.contents = []
        self.capacity = capacity

    def push(self, item):
        self.contents.append(item)

    def pop(self):
        if len(self.contents) == 0:
            popped = None
        else:
            popped = self.contents.pop()

        return popped

    def __repr__(self):
        return str(self.contents)


class SetOfStacks:
    def __init__(self):
        self.contents = []

    def push(self, item):
        try:
            last_stack = self.contents[-1]
        except IndexError:
            # there is nothing in the set of stacks
            last_stack = Stack(5)
            self.contents.append(last_stack)

        if len(last_stack.contents) == last_stack.capacity:
            new_stack = Stack(5)
            new_stack.push(item)
            self.contents.append(new_stack)
        else:
            last_stack.push(item)

    def pop(self):
        try:
            last_stack = self.contents[-1]
        except IndexError:
            # there is nothing in the set of stacks
            return None

        popped = last_stack.pop()
        if len(last_stack.contents) == 0:
            self.contents.pop()

        return popped

    def __repr__(self):
        return str(self.contents)


if __name__ == '__main__':
    setOfStacks = SetOfStacks()
    setOfStacks.push(20)
    print(repr(setOfStacks))

    for i in range(0, 6):
        setOfStacks.push(21)

    print(repr(setOfStacks))

    for i in range(0, 3):
        setOfStacks.pop()

    print(repr(setOfStacks))
