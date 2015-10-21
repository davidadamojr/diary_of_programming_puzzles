"""
Write an algorithm which computes the number of trailing zeros in n factorial.
"""

def count_trailing_zeros(n):
    """
    Each 5-multiple in the factorial (1x2x...xn) contributes a trailing zero
    5-multiples are 5, 25, 125, etc.
    """
    
    count = 0
    if n < 0:
        return -1 # error
    
    multiple = 5
    while n / multiple > 0:
        count = count + n / multiple
        multiple = multiple * 5
    
    return count

if __name__ == '__main__':
    print count_trailing_zeros(50)
        