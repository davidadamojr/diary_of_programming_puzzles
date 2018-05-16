"""
Merge two sorted linked lists and return it as a new list. The new list should 
be made by splicing together the nodes of the first two lists.

Leetcode question: https://leetcode.com/problems/merge-two-sorted-lists/
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# @param l1 first sorted list
# @param l2 second sorted list
def merge_two_lists(l1, l2):
    merged_list = []
    first_list_node = l1
    second_list_node = l2
    if l1 == None and l2 == None:
        return None

    while first_list_node != None and second_list_node != None:
        if first_list_node.val < second_list_node.val:
            if len(merged_list) != 0:
                merged_list[-1].next = first_list_node
            merged_list.append(first_list_node)
            first_list_node = first_list_node.next
        else:
            if len(merged_list) != 0:
                merged_list[-1].next = second_list_node
            merged_list.append(second_list_node)
            second_list_node = second_list_node.next

    # handle "leftovers"
    while first_list_node != None:
        if len(merged_list) != 0:
            merged_list[-1].next = first_list_node
        merged_list.append(first_list_node)
        first_list_node = first_list_node.next

    while second_list_node != None:
        if len(merged_list) != 0:
            merged_list[-1].next = second_list_node
        merged_list.append(second_list_node)
        second_list_node = second_list_node.next

    # return the head of the merged list   
    return merged_list[0]
