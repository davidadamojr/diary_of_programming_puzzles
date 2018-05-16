"""
Given two binary strings, return their sum (also as a binary string).

For example,
a = "11"
b = "1"

Return "100".
"""


# @param a, a string representing a binary number
# @param b, a string representing a binary number
# @param @return a string representing the sum of the two numbers
def add_binary(a, b):
    current_index = 0
    result = ""
    carry = 0
    while current_index < max(len(a), len(b)) or carry:
        current_a_digit = a[-1 - current_index] if current_index < len(a) else '0'
        current_b_digit = b[-1 - current_index] if current_index < len(b) else '0'
        value = to_int(current_a_digit) + to_int(current_b_digit) + carry

        result = "%s%s" % (value % 2, result)
        carry = 1 if value > 1 else 0

        current_index = current_index + 1

    return result


def to_int(character):
    if character == '1':
        return 1
    else:
        return 0


if __name__ == '__main__':
    print(add_binary("11", "1"));
    print(add_binary("1111", "1111111"))
