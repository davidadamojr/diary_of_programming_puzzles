"""
Remove all elements from a linked list of integers that have value "val".

Example:
Given: 1->2->6->3->4->5->6, val = 6
Return: 1->2->3->4->5
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# @param head, a reference to the head of the linked list
# @param val, the value to be removed from the linked list
def remove_elements(head, val):
    
    while head != None and head.val == val:
        head = head.next
        
    if head == None:
        return head
    
    current_node = head
    while current_node != None:
        while current_node.next != None and current_node.next.val == val:
            current_node.next = current_node.next.next
        
        current_node = current_node.next
    
    return head
            