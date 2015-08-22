"""
Given two strings s and t, write a function to determine if t is an anagram 
of s.

For example, 
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

You may assume the string only contains lowercase alphabets
"""

def is_anagram(s, t):
    # first check to see if the two strings are the same length
    # anagrams are of the same length
    
    if len(s) != len(t):
        return False
    
    letters_hash = {}
    for character in s:
        if character in letters_hash:
            letters_hash[character] = letters_hash[character] + 1
        else:
            letters_hash[character] = 1
    
    for character in t:
        if character in letters_hash and letters_hash[character] > 0:
            letters_hash[character] = letters_hash[character] - 1
        else:
            return False
    
    return True

if __name__ == '__main__':
    s = "anaba"
    t = "banaa"
    print is_anagram(s, t)
    
    s = "bulldozer"
    t = "bulldog"
    print is_anagram(s, t)
    