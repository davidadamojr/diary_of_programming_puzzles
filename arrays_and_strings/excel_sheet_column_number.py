"""
Given a column title as appears in an Excel sheet, return its corresponding 
column number.

For example:
A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28

Leetcode problem: https://leetcode.com/problems/excel-sheet-column-number/
"""

def title_to_number(column_title):
    # this is pretty much a base 26 number system
    # Horner's rule comes to mind
    if column_title.strip() == '':
        return 0
    
    char_map = {}
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in xrange(0, len(characters)):
        char_map[characters[i]] = i+1
    
    column_number = 0
    for j in xrange(0, len(column_title)):
        column_number = column_number * 26 + char_map[column_title[j]]
    
    return column_number

if __name__ == '__main__':
    print title_to_number('AA')
    print title_to_number('AAA')
    print title_to_number('ZZZ')