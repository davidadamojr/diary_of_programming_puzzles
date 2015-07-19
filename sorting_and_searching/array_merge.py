"""
You are given two sorted arrays A and B, where A has a large enough buffer at the 
end to hold B. Write a method to merge B into A in sorted order.
"""

# @param list_a a sorted list with enough space at the end for list_b
# @param list_b a sorted list to be merged with list_a
# @param list_a_index index of last element of list_a
def array_merge(list_a, list_b, last_a_index):
    """
    Start comparing values from the end of each array
    """
    list_a_length = len(list_a)
    list_b_length = len(list_b)
    
    last_b_index = list_b_length - 1 # index of last element in list_b
    last_merged_index = last_a_index + 1 + list_b_length - 1
    
    while last_b_index >= 0:
        if last_a_index >= 0 and list_a[last_a_index] > list_b[last_b_index]:
            list_a[last_merged_index] = list_a[last_a_index]
            last_a_index = last_a_index - 1
        else:
            list_a[last_merged_index] = list_b[last_b_index]
            last_b_index = last_b_index - 1
        
        last_merged_index = last_merged_index - 1
        
    return list_a

if __name__ == '__main__':
    list_a = [1,2,3,4,5,-1,-1,-1,-1,-1] # -1 values represent padding
    list_b = [1,8,15,16,17]
    print array_merge(list_a, list_b, 4)


    
    
    
    