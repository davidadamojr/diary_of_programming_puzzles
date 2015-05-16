"""
Write code to partition a linked list around a value x, such that all nodes
less than x come before all nodes greater than or equal to x
"""
from linked_list import LinkedListNode
import random

def partition(linked_list, by_value):
    if not linked_list:
        return None

    larger_than_list = None
    smaller_than_list = None

    current_node = linked_list
    while current_node != None:
        if current_node.data < by_value:
            if smaller_than_list == None:
                smaller_than_list = current_node
                last_smaller = smaller_than_list
            else:
                last_smaller.next = current_node
                last_smaller = current_node
        else:
            if larger_than_list == None:
                larger_than_list = current_node
                last_larger = larger_than_list
            else:
                last_larger.next = current_node
                last_larger = current_node

        current_node = current_node.next

    # test for nones
    if larger_than_list == None:
        last_smaller.next = None
        return smaller_than_list
    elif smaller_than_list == None:
        last_larger.next = None
        return larger_than_list
    else:
        last_smaller.next = larger_than_list
        last_larger.next = None
        return smaller_than_list



root = LinkedListNode(5)
current_node = root
for i in range(0, 10):
    random_key = random.randint(0, 10)
    new_node = LinkedListNode(random_key)
    current_node.next = new_node
    current_node = new_node
    if i == 4:
        middle_node = current_node.data

print "Original list: " + str(root)
print "Partitioned list: " + str(partition(root, middle_node))
