"""
Given a sorted (increasing order) array with unique integer elements, write 
an algorithm to create a binary search tree with minimal height.
"""
from tree import Tree

# @param list_of_integers a list of sorted integers in ascending order
# @param start starting index of list
# @param end ending index of list
def create_minimal_bst(list_of_integers, start, end):
    if end < start:
        return None
    
    # get the middle element of the list
    middle = (start + end) / 2
    root = Tree(list_of_integers[middle], create_minimal_bst(list_of_integers, start, middle-1),
                create_minimal_bst(list_of_integers, middle+1, end))
    return root

if __name__ == '__main__':
    binary_search_tree = create_minimal_bst([2,4,6,7,92,101,333,334,888], 0, 8)
    print binary_search_tree
    
    