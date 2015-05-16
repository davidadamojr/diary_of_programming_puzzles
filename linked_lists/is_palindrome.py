"""
Implement a function to check if a linked list is a palindrome
"""
import random
from linked_list import LinkedListNode

def is_palindrome1(linked_list):
    # reverse and compare
    pass

def build_palindrome_list():
    root = LinkedListNode(5)
    previous_node = root
    for i in range(0, 2):
        new_node = LinkedListNode(random.randint(0, 9))
        previous_node.next = new_node
        previous_node = new_node

    stack = []
    current_node = root
    while current_node.next != None: # all but the last one
        stack.append(current_node.data)
        current_node = current_node.next

    while len(stack) != 0:
        data = stack.pop()
        new_node = LinkedListNode(data)
        previous_node.next = new_node
        previous_node = new_node

    return root




def build_random_list():
    pass