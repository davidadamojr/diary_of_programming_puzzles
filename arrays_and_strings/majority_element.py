"""
Given an array of size n, find the majority element. The majority element is 
the element that appears more than floor(n/2) times.

You may assume that the array is non-empty and the majority element always 
exists in the array.

Leetcode question: https://leetcode.com/problems/majority-element/
"""

def majority_element(input_list):
    majority = len(input_list) / 2
    appearance_map = {}
    for i in xrange(0, len(input_list)):
        if input_list[i] in appearance_map:
            appearance_map[input_list[i]] = appearance_map[input_list[i]] + 1
        else:
            appearance_map[input_list[i]] = 1
    
    for element in appearance_map:
        if appearance_map[element] > majority:
            return element
    
    return 0

if __name__ == '__main__':
    print majority_element([1,2,3,4,5,5,5,5,5,5,6])