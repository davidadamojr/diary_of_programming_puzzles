"""
Write a function that adds two numbers. You should not use + or any
arithmetic operators.
"""


def add(first_number, second_number):
    if second_number == 0:
        return first_number

    # first add without considering "carry" - this is equivalent to XOR
    sum_without_carry = first_number ^ second_number

    # then add with only the "carry" - this is equivalent to AND and left shift 1
    carry = (first_number & second_number) << 1

    # add the sum without carry and the carry
    # need to recurse since you are not allowed to use arithmetic operators
    return add(sum_without_carry, carry)


print(str(add(10, 15)))
