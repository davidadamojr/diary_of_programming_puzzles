"""
An implementation of the Knuth-Morris-Pratt (KMP) string matching algorithm
The KMP algorithm spends a little time precomputing a table (on the order of the 
size of W[], O(n)) and then uses the table to do an efficient search of the string 
in O(k). KMP makes use of previous match information.
"""


# @param pattern string the pattern to be searched for
def build_table(pattern):
    prefix_table = [0 for character in pattern]
    current_position = 2  # current position of table we are computing
    substring_position = 0  # zero-based index in pattern of the next character of the candidate substring
    prefix_table[0] = -1
    prefix_table[1] = 0

    while current_position < len(pattern):
        # first case: next character and previous character of the substring are the same
        if pattern[current_position - 1] == pattern[substring_position]:
            substring_position = substring_position + 1
            prefix_table[current_position] = substring_position
            current_position = current_position + 1

        # second case: substring does not continue
        elif substring_position > 0:
            substring_position = prefix_table[substring_position]

        # third case: no more candidate substrings
        else:
            prefix_table[current_position] = 0
            substring_position = substring_position + 1

    return prefix_table


# @param pattern string the string pattern to be searched for
# @param text string the string to be searched
def kmp_search(pattern, text):
    current_match_index = 0  # the beginning of the current match in text
    current_char_index = 0  # the position of the current character in pattern
    prefix_table = build_table(pattern)

    while current_match_index + current_char_index < len(text):
        if pattern[current_char_index] == text[current_match_index + current_char_index]:
            if current_char_index == len(pattern) - 1:
                return current_match_index
            current_char_index = current_char_index + 1
        else:
            # current character in pattern failed to match corresponding character in text
            if prefix_table[current_char_index] > -1:
                current_match_index = current_match_index + current_char_index - prefix_table[current_char_index]
                current_char_index = prefix_table[current_char_index]
            else:
                current_char_index = 0
                current_match_index = current_match_index + 1


if __name__ == '__main__':
    print(kmp_search("aab", "aaaaaaaaaaaaaaaaaaaab"))
