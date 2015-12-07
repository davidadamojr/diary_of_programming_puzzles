"""
Write a function to find the longest common prefix string amongst an array 
of strings
"""

# @param {list} list of strings
# @return {string} string representing the longest common prefix
def longest_common_prefix(string_lst):
    if not string_lst:
        return ""
    
    # find shortest string length first
    shortest = len(string_lst[0])
    for string in string_lst:
        length = len(string)
        if length < shortest:
            shortest = length
            
    # compare each character of each string
    longest_prefix = ""
    for str_index in range(0, shortest):
        current_char = string_lst[0][str_index]
        for lst_index in range(1, len(string_lst)):
            if string_lst[lst_index][str_index] != current_char:
                return longest_prefix
        
        longest_prefix = longest_prefix + current_char
    
    return longest_prefix

if __name__ == '__main__':
    print longest_common_prefix(["beet", "bee", "beep", "bet"])