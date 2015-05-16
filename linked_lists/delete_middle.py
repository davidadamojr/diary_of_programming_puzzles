"""
Implement an algorithm to delete a node in the middle of a singly linked list,
given only access to that node
"""
from linked_list import LinkedListNode
import random

def delete_middle(middle_node):
    """
    Since you are not given access to the head of the list, you can simply
    copy the data from the next node to the current node and then delete the
    next node.
    This solution does not work if the node to be deleted is the last node.
    """
    middle_node.data = middle_node.next.data
    middle_node.next = middle_node.next.next



root = LinkedListNode(5)
current_node = root
for i in range(0, 10):
    random_key = random.randint(0, 10)
    new_node = LinkedListNode(random_key)
    current_node.next = new_node
    current_node = new_node
    if i == 4:
        middle_node = current_node

print "Original list: " + str(root)
delete_middle(middle_node)
print "List with middle node deleted: " + str(root)