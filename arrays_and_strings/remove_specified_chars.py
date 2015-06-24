"""
Write an efficient function that deletes characters from an ASCII string.
Use the prototype:

    removeChars(string str, string remove);

where any character existing in "remove" must be deleted from "str". For example,
given a "str" of "Battle of the Vowels: Hawaii vs. Grozny" and a "remove" of
"aeiou", the function should transform str to "Bttl f th Vwls: Hw vs. Grzny".
"""

def remove_specified_chars1(string, removechars):
    """
    uses a hash table for "removechars" lookup instead of linearly checking 
    the "removechars" string each time
    
    Builds up a new string - not very space efficient
    """
    if string == "" or removechars == "":
        return string

    new_string = ""
    chars_dict = {}
    for rem_char in removechars:
        if rem_char not in chars_dict:
            chars_dict[rem_char] = 1

    for string_char in string:
        if string_char not in chars_dict:
            new_string = new_string + string_char

    return new_string

def remove_specified_chars2(string, removechars):
    """
    * uses a hash table for removechars lookup and writes the new string in place 
    instead of using a buffer
    * Advances a destination pointer on the string itself for characters that are 
    not removed, does not advance the pointer for strings to be deleted
    * Based on the idea that after checking a particular character and moving on, 
    you do not need it any more and it can be replaced
    """
    if string == "" or removechars == "":
        return string

    chars_dict = {}
    string_list = list(string)
    for rem_char in removechars:
        if rem_char not in chars_dict:
            chars_dict[rem_char] = 1

    src_index = 0
    dest_index = 0
    for src_index in xrange(0, len(string_list)):
        if string_list[src_index] not in chars_dict:
            string_list[dest_index] = string_list[src_index]
            dest_index = dest_index + 1

    return ''.join(string_list[0:dest_index+1])

print remove_specified_chars1('Battle of the Vowels: Hawaii vs. Grozny', 'aeiou')
print remove_specified_chars2('Battle of the Vowels: Hawaii vs. Grozny', 'aeiou')




