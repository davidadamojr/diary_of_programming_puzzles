"""
Given an integer, write an algorithm to convert it to hexadecimal. For negative integers, two's complement method is
used.

Note:
1. All letters in hexadecimal (a-f) must be in lowercase.
2. The hexadecimal string must not contain extra leading 0s. If the number is zero, it is represented by a single zero
character '0'; otherwise, the first character in the hexadecimal string will not be zero character.
3. The given number is guaranteed to fit within the range of a 32-bit signed integer.
4. You must not use any method provided by the library which converts/formats the number to hex directly.

Example 1:
Input:
26

Output:
"1a"

Example 2:
Input:
-1

Output:
"ffffffff"
"""

# @param num the number to convert to hexadecimal
# @return the hexadecimal representation of the number
def to_hex(num):
    if num == 0:
        return "0"

    hex_digits = {
        10 : "a",
        11 : "b",
        12 : "c",
        13 : "d",
        14 : "e",
        15 : "f"
    }

    hex_num = ""

    is_negative = False
    if num < 0:
        magnitude = abs(num)
        mask = ((1 << 32) - 1) + (1 << 32)
        inverted = magnitude ^ mask
        num = inverted + 1
        is_negative = True

    while num != 0:
        remainder = num % 16
        num = num / 16

        if remainder in hex_digits:
            hex_num = hex_digits[remainder] + hex_num
        else:
            hex_num = str(remainder) + hex_num

    if is_negative:
        return hex_num[1:]

    return hex_num

if __name__ == '__main__':
    assert to_hex(0) == "0"
    assert to_hex(-1) == "ffffffff"
    assert to_hex(26) == "1a"
    print "All test cases passed successfully."