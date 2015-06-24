"""
Write an efficient function to find the first non-repeated character in a string.
For instance, the first nonrepeated character in "total" is 'o' and the first
nonrepeated character in "teeter" is r.
"""
def findFirstNonRepeated(string):
    """
    create a dictionary that maps each character to the number of times it occurs and then do a O(1) lookup - O(n) runtime
    """
    char_dict = {}
    for character in string:
        if character in char_dict:
            char_dict[character] = char_dict[character] + 1
        else:
            char_dict[character] = 1

    for character in string:
        if char_dict[character] == 1:
            return character

    return None

print findFirstNonRepeated("teet")


