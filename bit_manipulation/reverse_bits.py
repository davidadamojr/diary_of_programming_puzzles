"""
Reverse bits of a given 32-bit unsigned integer.

For example, given input 43261596 (represented in binary as 
00000010100101000001111010011100), return 964176192 (represented in binary as 
00111001011110000010100101000000).
"""


# @param n, an integer
# @return an integer
def reverse_bits(n):
    """
    Repeatedly shift right and bitwise and each bit to 1
    If the bit is 0, then the bitwise and operation is 0
    If the bit is 1, then the bitwise and operation is 1
    """

    if n == 0:
        return 0

    current_value = n
    reversed_bin_string = ""
    for i in range(0, 32):
        if current_value & 1 == 1:
            reversed_bin_string = reversed_bin_string + "1"
        else:
            reversed_bin_string = reversed_bin_string + "0"

        current_value = current_value >> 1

    return int(reversed_bin_string, 2)


if __name__ == '__main__':
    print(reverse_bits(43261596))
