"""
You have two numbers represented by a linked list, where each node contains
a single digit. The digits are stored in reverse order, such that the 1's
digit is at the head of the list. Write a function that adds the two numbers
and returns the sum as a linked list.

Suppose the digits are stored in forward order. Repeat the above problem.
"""

import random
from linked_list import LinkedListNode


def linked_list_add(first_linked_list, second_linked_list, carry):
    """
    The numbers are stored in reverse order
    """
    if not first_linked_list and not second_linked_list and carry == 0:
        return None

    value = carry
    if first_linked_list:
        value = value + first_linked_list.data

    if second_linked_list:
        value = value + second_linked_list.data

    result = value % 10  # the last digit
    result_linked_list = LinkedListNode(result)

    if first_linked_list or second_linked_list:
        next_node = linked_list_add(None if not first_linked_list else first_linked_list.next,
                                    None if not second_linked_list else second_linked_list.next,
                                    0 if value < 10 else 1)

        result_linked_list.next = next_node

    return result_linked_list


def linked_list_add_forward(linked_list_one, linked_list_two, carry):
    # convert the first list to an integer
    current_node = linked_list_one
    first_integer_value = 0
    while current_node:
        first_integer_value = first_integer_value * 10 + current_node.data
        current_node = current_node.next

    current_node = linked_list_two
    second_integer_value = 0
    while current_node:
        second_integer_value = second_integer_value * 10 + current_node.data
        current_node = current_node.next

    result = first_integer_value + second_integer_value

    # convert result back to a linked list
    divided_by_ten = result
    next_node = None
    while divided_by_ten != 0:
        current_digit = divided_by_ten % 10
        divided_by_ten = divided_by_ten / 10
        new_node = LinkedListNode(current_digit)
        new_node.next = next_node
        next_node = new_node

    return new_node


def create_random_linked_list(number_of_nodes):
    root = LinkedListNode(random.randint(0, 9))
    current_node = root
    for i in range(0, number_of_nodes - 1):
        random_key = random.randint(0, 9)
        new_node = LinkedListNode(random_key)
        current_node.next = new_node
        current_node = new_node

    return root


first_number = create_random_linked_list(4)
second_number = create_random_linked_list(4)
print("First number: " + str(first_number))
print("Second number: " + str(second_number))
print(str(linked_list_add(first_number, second_number, 0)))
print("===================================================")

print("First number: " + str(first_number))
print("Second number: " + str(second_number))
print(str(linked_list_add_forward(first_number, second_number, 0)))
