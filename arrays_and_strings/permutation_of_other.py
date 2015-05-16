"""
Given two strings, write a function to determine if one is a permutation
of the other

Considerations: is comparison case sensitive? Is whitespace significant?
"""
def is_permutation(first_string, second_string):
    """
    The strings cannot be permutations of one another if they are not of the
    same length
    """
    length_of_first = len(first_string)
    length_of_second = len(second_string)
    if length_of_first <> length_of_second:
        return False

    # sort both strings and compare them
    first_string_sorted = ''.join(sorted(first_string))
    second_string_sorted = ''.join(sorted(second_string))

    for i in range(0, len(first_string_sorted)):
        if first_string_sorted[i] <> second_string_sorted[i]:
            return False

    return True

def is_permutation_2(first_string, second_string):
    """
    Another way to approach this problem is to keep track of character
    counts - this approach is more efficient but less understandable than
    the previous approach
    """
    length_of_first = len(first_string)
    length_of_second = len(second_string)
    if length_of_first <> length_of_second:
        return False

    character_dict = {}
    for character in first_string:
        if character in character_dict:
            character_dict[character] = character_dict[character] + 1
        else:
            character_dict[character] = 1

    for character in second_string:
        if character in character_dict:
            character_dict[character] = character_dict[character] - 1
            if character_dict[character] < 0:
                return False
        else:
            return False

    return True



print is_permutation("dane", "enad")
print is_permutation("dragon", "dracon")
print is_permutation("danee", "ednae")
print is_permutation("draconian", "cdraafian")
print " "
print is_permutation_2("dane", "enad")
print is_permutation_2("dragon", "dracon")
print is_permutation_2("danee", "ednae")
print is_permutation_2("draconian", "cdraafian")