"""
Implement an algorithm to determine if an algorithm contains all unique
characters? What if you cannot use any additional data structures?

- In Java, you can use a boolean array of length 128 (for ascii)
"""
def unique_characters(my_string):
    if my_string == "":
        return True

    character_count = {}
    for character in my_string:
        if character in character_count:
            return False
        else:
            character_count[character] = 1

    return True

def unique_characters_no_ds(my_string):
    """
    Implementing a solution to this problem without an additional data structure
    requires using bit manipulation
    """
    checker = 0
    for character in my_string:
        char_code = ord(character) - ord('a')
        one_left_shift = 1 << char_code
        if checker & one_left_shift > 0:
            return False

        checker = checker | one_left_shift

    return True

if unique_characters("dane"):
    print "The characters are unique"

if unique_characters_no_ds("dane"):
    print "The characters are unique"






