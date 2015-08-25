"""
Given a string, determine if it is a palindrome, considering only alphanumeric 
characters and ignoring cases.

For example, 
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Empty strings are valid palindromes.
"""

# @param s {string} the string to be tested
def is_palindrome(s):
    start = 0
    end = len(s) - 1
    
    while start < end:
        start_character = s[start].lower()
        end_character = s[end].lower()
        if not start_character.isalnum():
            start = start + 1
            continue
        
        if not end_character.isalnum():
            end = end - 1
            continue
        
        if start_character != end_character:
            return False
            
        start = start + 1
        end = end - 1
    
    return True

if __name__ == '__main__':
    my_string = "A man, a plan, a canal: Panama";
    print is_palindrome(my_string)

