"""
Given a string s consists of upper/lower-case alphabets and empty space characters 
' ', return the length of the last word in the string.
If the last word does not exist, return 0.

Note: A word is defined as a character sequence that consist of non-space 
characters only.
For example, 

Given s = "Hello World", return 5.

Leetcode problem: https://leetcode.com/problems/length-of-last-word/
"""

def last_word_length(input_string):
    # linear time solution
    
    trimmed_string = input_string.strip()
    if trimmed_string == "":
        return 0
    
    # start at the end of the string
    position = len(trimmed_string) - 1
    while position >= 0:
        if trimmed_string[position] == " ":
            break
        
        position = position - 1
    
    last_word = trimmed_string[position+1:]
    return len(last_word)

if __name__ == '__main__':
    print last_word_length("Hello World")
    print last_word_length("To   whom  much is given  ")
    print last_word_length("")
    
    
    