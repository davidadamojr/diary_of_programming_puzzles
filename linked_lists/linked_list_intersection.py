"""
Write a program to find the node at which the intersection of two singly 
linked lists begins.

For example, the following two linked lists:

A: a1 -> a2 -> c1 -> c2 -> c3
B: b1 -> b2 -> b3 -> c1 -> c2 -> c3

begin to intersect at node c1.

Notes:
* If two linked lists have no intersection at all, return null.
* The linked lists must retain their original structure after the function returns
* You may assume there are no cycles anywhere in the entire linked structure
* Your code should preferably run in O(n) time and use only O(1) memory.

Leetcode problem: https://leetcode.com/problems/intersection-of-two-linked-lists/
"""

def get_intersection_node(headA, headB):
    # figure out the difference in length of the two linked lists
    # then use that information to traverse the two lists in sync looking out 
    # for when there is an intersection
    # O(n)
    
    lista_length = 0
    listb_length = 0
    
    current_node = headA
    while current_node:
        lista_length = lista_length + 1
        current_node = current_node.next
    
    current_node = headB
    while current_node:
        listb_length = listb_length + 1
        current_node = current_node.next
    
    if lista_length > listb_length:
        longest = headA
        shorter = headB
    else:
        longest = headB
        shorter = headA
        
    difference = abs(lista_length - listb_length)
    
    lista_index = 0
    listb_index = 0
    
    current_node = longest
    while lista_index < difference:
        current_node = current_node.next            
        lista_index = lista_index + 1
    
    intersection = None
    current_other_node = shorter
    while current_other_node:
        if current_other_node == current_node:
            intersection = current_other_node
            break
        
        current_other_node = current_other_node.next
        current_node = current_node.next
    
    return intersection