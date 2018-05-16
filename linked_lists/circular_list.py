"""
Given a circular linked list, implement an algorithm which returns the node
at the beginning of the loop

THIS DOES NOT WORK
"""
import random
from linked_list import LinkedListNode


def create_circular_list(length_before_loop, loop_length):
    root = LinkedListNode(random.randint(0, 9))
    previous_node = root

    # create the section before the loop
    for i in range(0, length_before_loop):
        new_node = LinkedListNode(random.randint(0, 10))
        previous_node.next = new_node
        previous_node = new_node

    # this is the node the loop points to
    loop_back_node = previous_node
    print("The beginning of the loop is: " + str(loop_back_node))

    # create the nodes in the loop
    for i in range(0, loop_length):
        new_node = LinkedListNode(random.randint(0, 10))
        previous_node.next = new_node
        previous_node = new_node

    # create the cycle - point the end of the linked list back to the
    # "loop back node"
    previous_node.next = loop_back_node

    return root


def find_loop_beginning(circular_linked_list):
    """
    This requires a "fast pointer" and a "slow pointer". Fast pointer moves
    two steps at a time, slow pointer moves one step at a time
    """
    fast_pointer = circular_linked_list
    slow_pointer = circular_linked_list

    """
    When fast pointer and slow pointer collide, move slow pointer to the head
    of the list
    """
    while True:
        fast_pointer = fast_pointer.next.next
        slow_pointer = slow_pointer.next

        if fast_pointer == slow_pointer:
            slow_pointer = circular_linked_list
            break

    # move fast pointer and slow pointer one step at a time and return the
    # new collision point
    while fast_pointer != slow_pointer:
        fast_pointer = fast_pointer.next
        slow_pointer = slow_pointer.next

        if fast_pointer == slow_pointer:
            break

    return fast_pointer


circular_list = create_circular_list(5, 4)
# print find_loop_beginning(circular_list)
