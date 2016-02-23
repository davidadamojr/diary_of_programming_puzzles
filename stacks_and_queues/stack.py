"""
Implementation of stack data structure
"""

class Stack:
    def __init__(self):
        self.contents = []
    
    def peek(self):
        if self.is_empty():
            raise StackEmptyException
        else:
            return self.contents[-1]
            
    def pop(self):
        if self.is_empty():
            raise StackEmptyException
        else: 
            return self.contents.pop()
    
    def push(self, item):
        self.contents.append(item)
    
    def is_empty(self):
        return self.contents == []
    
    def size(self):
        return len(self.contents)

class StackEmptyException(Exception):
    pass