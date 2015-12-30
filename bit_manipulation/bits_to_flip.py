"""
Write a function to determine the number of bits you would need to flip 
to convert integer A to integer B
"""

def bits_to_flip(first_int, second_int):
    # the XOR of the two integers produces another integer whose 1 bits represent 
    # the bits that are different in the two numbers
    different_bits = first_int ^ second_int
    
    # count number of 1 bits in XOR
    bit_count = 0
    while different_bits != 0:
        if different_bits & 1 == 1:
            bit_count = bit_count + 1
        different_bits = different_bits >> 1
    
    return bit_count

if __name__ == '__main__':
    print bits_to_flip(88, 60)
        