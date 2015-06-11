"""
Given a positive integer, return its corresponding column title as it appears 
in an Excel sheet.

For example:
1 -> A
2 -> B
3 -> C
...
26 -> Z
27 -> AA
28 -> AB
"""

def convert_to_title(num):
    integer_map = {}
    characters = "ZABCDEFGHIJKLMNOPQRSTUVWXY"
    for i in xrange(0, 26):
        integer_map[i] = characters[i]
    
    column_title = ""
    while num <> 0:
        remainder = num % 26
        num = num - 1
        num = num / 26
        column_title = integer_map[remainder] + column_title
    
    return column_title

if __name__ == '__main__':
    print convert_to_title(703)
    print convert_to_title(27)
    print convert_to_title(26)