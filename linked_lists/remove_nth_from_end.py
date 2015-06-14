"""
Given a linked list, remove the nth node from the end of the list and return 
its head.

For example,
Given the linked list: 1->2->3->4->5, and n = 2.
After removing the second node from the end, the linked list becomes 
1->2->3->5.

Note:
Given n will always be valid.
Try to do this in one pass
"""

# @param head a reference to the head of the list
# @param n the position (from the tail) of the node that should be deleted
# @return a new linked list with the required node deleted
def remove_nth_from_end(head, n):
    n_behind_node = head
    faster_node = head
    before_behind_node = head
    
    for i in xrange(0, n):
        faster_node = faster_node.next
    
    while faster_node:
        faster_node = faster_node.next
        before_behind_node = n_behind_node
        n_behind_node = n_behind_node.next
    
    # handle situation where there is only one node in the linked list or the 
    # head is the one being removed
    if before_behind_node == n_behind_node:
        if not n_behind_node.next:
            head = None
        else:
            head = n_behind_node.next
    else:
        before_behind_node.next = before_behind_node.next.next
    
    return head
            