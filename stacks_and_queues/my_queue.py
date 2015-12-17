"""
Implement a MyQueue class which implements a queue using two stacks.
"""

from stack import Stack

class MyQueue:
    def __init__(self):
        self.new_elements = Stack()
        self.old_elements = Stack()
    
    def enqueue(self, element):
        self.new_elements.push(element)
    
    def dequeue(self, element):
        if self.old_elements.is_empty():
            self.move_elements()
        
        return self.old_elements.pop()
    
    def move_elements(self):
        while not self.new_elements.is_empty():
            element = self.new_elements.pop()
            self.old_elements.push(element)
    
    def size(self):
        return self.new_elements.size() + self.old_elements.size()