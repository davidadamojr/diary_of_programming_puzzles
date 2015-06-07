"""
Given a string containing just the characters '(', ')', '{', '}', '[', ']',
determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid 
but "(]" and "([)]" are not.

Leetcode problem: https://leetcode.com/problems/valid-parentheses/
"""

def is_valid_parentheses(input_string):
    character_map = {'(':')', '{':'}', '[':']'}
    stack = []
    string_list = list(input_string)
    string_is_valid = True
    for character in string_list:
        if character == '(' or character == '{' or character == '[':
            stack.append(character)
        else:
            if len(stack) == 0:
                return False
            
            top = stack.pop()
            if character_map[top] != character:
                return False
            
    
    if len(stack) != 0:
        return False
    
    return string_is_valid

if __name__ == '__main__':
    print is_valid_parentheses("{{}}")
    print is_valid_parentheses("[[{]]{")
    print is_valid_parentheses("[")
