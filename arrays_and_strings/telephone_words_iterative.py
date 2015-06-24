"""
Given a mapping of numbers to letters on a telephone keypad, write a function that 
takes a seven-digit telephone number and prints out all the possible "words" or 
combinations of letters that can represent the given number. The 0 and 1 
keys do not map to any letters, so you should change only the digits 2-9 to letters.
You will be passed an array of seven integers, with each element being one digit 
in the number. You may assume that only valid phone numbers will be passed to 
your function. 

There is a recursive solution to this problem, but it is inefficient - O(3^n)
"""

key_strings = {'2': 'abc',
               '3': 'def',
               '4': 'ghi',
               '5': 'jkl',
               '6': 'mno',
               '7': 'prs',
               '8': 'tuv',
               '9': 'wxy'}

def get_char_key(key, place):
    is_one = key == '1';
    is_zero = key == '0';
    if is_one:
        return '1'
    elif is_zero:
        return '0'
    else:
        return key_strings[key][place-1]

def translate_number(phone_number):
    phone_number_length = len(phone_number)
    translation = []

    for i in range(0, phone_number_length):
        translation.append(get_char_key(phone_number[i], 1))

    while 1:
        # infinite loop that breaks when all the numbers are at their "high" value
        print ''.join(translation)

        for i in range(phone_number_length-1, -2, -1):
            if i == -1:
                # once it goes past the leftmost digit, we are done
                return

            is_one = phone_number[i] == '1'
            is_zero = phone_number[i] == '0'
            is_high = get_char_key(phone_number[i], 3) == translation[i]
            is_low = get_char_key(phone_number[i], 1) == translation[i]
            is_medium = get_char_key(phone_number[i], 2) == translation[i]
            if is_high or is_one or is_zero:
                translation[i] = get_char_key(phone_number[i], 1)
                #no break, continue to left neighbor
            elif is_low:
                translation[i] = get_char_key(phone_number[i], 2)
                break
            elif is_medium:
                translation[i] = get_char_key(phone_number[i], 3)
                break

translate_number("5955942")



