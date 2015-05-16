"""
Given a real number between 0 and 1 (e.g. 0.72) that is passed in as a double,
print the binary representation. If the number cannot be represented accurately
in binary with at most 32 characters, print "ERROR"
"""

def get_binary_rep(real_number):
    """
    Compare the number to 0.5, 0.25, ...
    This is based on the idea that each binary digit after the decimal point
    represents successive divisions of the digit by powers of 2
    """
    if real_number > 1 or real_number < 0:
        return "ERROR"

    binary_rep = "."
    fraction = 0.5
    while real_number > 0:
        if len(binary_rep) > 32:
            return "ERROR"

        if real_number > fraction:
            binary_rep = binary_rep + "1"
        else:
            binary_rep = binary_rep + "0"

        real_number = real_number - fraction
        fraction = fraction / 2

    return binary_rep

print get_binary_rep(0.72)



