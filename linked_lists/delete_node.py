"""
Write a function to delete a node (except the tail) in a singly linked list,
given only access to that node.

Suppose the linked list is 1 -> 2 -> 3 -> 4 and you are given the third node 
with value 3, the linked list should become 1 -> 2 -> 4 after calling your function.

https://leetcode.com/problems/delete-node-in-a-linked-list/
"""

from linked_list import LinkedListNode

# @param head LinkedListNode the head of a linked list
# @param node LinkedListNode the linked list node to be deleted
def delete_node(node):
    if node and node.next:
        node.data = node.next.data
        node.next = node.next.next

if __name__ == '__main__':
    head = LinkedListNode(1)
    head.next = LinkedListNode(2)
    head.next.next = LinkedListNode(3)
    head.next.next.next = LinkedListNode(4)
    
    delete_node(head.next.next)
    assert str(head) == "1, 2, 4"
    print "All test cases passed." 