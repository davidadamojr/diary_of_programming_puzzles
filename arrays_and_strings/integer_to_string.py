"""
Write a routine to convert a signed integer into a string.
"""
def integer_to_string(integer):
    """
    Writes the string backward and reverses it
    """
    if integer < 0:
        is_negative = True
        integer = -integer #for negative integers, make them positive
    else:
        is_negative = False

    integer_string = ""
    while integer != 0:
        new_digit = integer % 10
        
        # "ord" returns the character code of its argument
        ascii_code = ord('0') + new_digit 
        
        # "chr" returns the string representation of its argument
        integer_string = integer_string + chr(ascii_code)

        integer = integer / 10

    # in python, the easiest way to reverse a string is "string[::-1]"\
    integer_string = '-' + integer_string[::-1] if is_negative else integer_string[::-1]
    
    return integer_string

if __name__ == "__main__":
    print integer_to_string(-1234)
    print integer_to_string(54321)