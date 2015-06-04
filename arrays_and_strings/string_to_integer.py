def string_to_integer1(string):
    """
    Start at the left end (beginning) of the string
    Multiply the ascii value of each character - ascii value of 0 to get the current character's numerical value
    Start with the numerical value of the first character
    Then multiply the numerical value of the current character by 10 and add the next number

    Horner's rule - most straightforward approach
    """
    if string == '':
        return None

    is_negative = False
    start = 0
    if string[0] == '-':
        is_negative = True
        start = 1

    integer_value = 0
    for index in range(start, len(string)):
        character_int = ord(string[index]) - ord('0')
        integer_value = integer_value * 10 + character_int

    if is_negative:
        integer_value = -integer_value

    return integer_value

def string_to_integer2(string):
    """
    Start at the right end of string, starting with a place value of 1
    Multiply the place value by 10 with each iteration
    """
    place_value = 1
    integer_value = 0
    end = len(string) - 1
    start = 0
    if string[0] == '-':
        isNegative = True
        start = 1
    else:
        isNegative = False

    while end >= start:
        current_value = ord(string[end]) - ord('0')
        integer_value = integer_value + current_value * place_value
        place_value = place_value * 10
        end = end - 1

    if isNegative:
        integer_value = -integer_value

    return integer_value


print string_to_integer1("-234")
print string_to_integer1("234")
print string_to_integer2("234")
print string_to_integer2("-234")












