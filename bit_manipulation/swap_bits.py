"""
Write a program to swap odd and even bits in an integer with as few instructions 
as possible (e.g. bit 0 and bit 1 are swapped, bit 2 and bit 3 are swapped, 
and so on. 
"""

def swap_bits(num):
    return ((num & 0xaaaaaaaaaaaaaaaaa) >> 1) | ((num & 0x5555555555555555) << 1)

if __name__ == '__main__':
    assert bin(swap_bits(9)) == "0b110"
    print "All test cases passed successfully."
    

