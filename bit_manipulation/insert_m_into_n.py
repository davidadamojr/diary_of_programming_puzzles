"""
You are given two 32-bit numbers, N and M, and two bit positions, i and j.
Write a method to insert M into N such that M starts at bit j and ends at
bit i. You can assume that the bits j through i have enough space to fit all
of M. That is, if M = 10011, you can assume that there are at least 5 bits
between j and i. You would not, for example, have j=3 and i=2, because M could
fully fit between bit 3 and bit 2
"""

def updateBits(n, m, j, i):
    # clear bits j through i
    all_ones = ~0
    ones_before_j = all_ones << (j+1)
    ones_after_i = (1 << i) - 1
    mask = ones_before_j | ones_after_i
    n_cleared = n & mask

    aligned_m = m << i

    inserted = n | aligned_m

    return inserted

print bin(updateBits(1024, 19, 6, 2))