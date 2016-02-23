"""
Write a program to sort a stack in ascending order (with biggest items on top). 
You may use at most one additional stack to hold items, but you may not copy 
the elements into any other data structure (such as an array). The stack 
supports the following operations: push, pop, peek and isEmpty.
"""

from stack import Stack
from stack import StackEmptyException

def build_unsorted_stack():
    unsorted_stack = Stack()
    unsorted_stack.push(10)
    unsorted_stack.push(5)
    unsorted_stack.push(12)
    unsorted_stack.push(8)
    unsorted_stack.push(3)
    return unsorted_stack

def sort_stack(unsorted_stack):
    """
    Use an additional stack. Pop the top element from the unsorted stack and 
    compare to all elements in the sorted stack until you find an element less 
    than the element you are currently considering. Once you find this element, 
    add the new element above that one.
    """
    
    sorted_stack = Stack()
    
    while not unsorted_stack.is_empty():
        try:
            unsorted_top = unsorted_stack.pop()
            if sorted_stack.is_empty():
                sorted_stack.push(unsorted_top)
            else:
                while not sorted_stack.is_empty():
                    sorted_top = sorted_stack.peek()
                    if unsorted_top < sorted_top:
                        unsorted_stack.push(sorted_stack.pop())
                    elif unsorted_top >= sorted_top:
                        sorted_stack.push(unsorted_top)
                        break
                
                if sorted_stack.is_empty():
                    sorted_stack.push(unsorted_top)
                    
        except StackEmptyException:
            raise StackEmptyException
    
    return sorted_stack
            
        

if __name__ == '__main__':
    unsorted_stack = build_unsorted_stack()
    try:
        print "Unsorted stack: ", unsorted_stack.contents
        print "Sorted stack: ", sort_stack(unsorted_stack).contents
    except StackEmptyException:
        print "An error occurred."