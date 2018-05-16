"""
Write a program that reverses a linked list without using more than O(1) storage
"""
from linked_list import LinkedListNode
import random

head = LinkedListNode(random.randint(0, 20))
previous = head
for i in range(0, 5):
    node = LinkedListNode(random.randint(0, 20))
    previous.next = node
    previous = node

node.next = None

print(head)

current = head
next = current.next
current.next = None
while next:
    old_next = next.next
    next.next = current
    current = next
    next = old_next

print(current)
