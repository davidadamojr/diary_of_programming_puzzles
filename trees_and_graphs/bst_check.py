"""
Implement a function to check if a binary tree is a binary search tree.
"""
from trees import *
import sys

def build_valid_binary_tree():
    root = TreeNode(20)
    bintree = BinarySearchTree(root)
    bintree.insert(10)
    bintree.insert(30)
    bintree.insert(5)
    bintree.insert(15)
    bintree.insert(3)
    bintree.insert(7)
    bintree.insert(17)

    return bintree

def build_invalid_binary_tree():
    root = TreeNode(20)
    root.left = TreeNode(500)
    bintree = BinarySearchTree(root)
    bintree.insert(10)
    bintree.insert(30)
    bintree.insert(5)
    bintree.insert(15)
    bintree.insert(3)
    bintree.insert(7)
    bintree.insert(17)

    return bintree

# @param bintree the binary tree to be checked
# @return true if bintree is a valid binary tree, false otherwise
def is_binary_tree(bintree_node, min, max):
    # perform a depth first search while checking the rules of a binary tree
    # pass down the restrictions (min and max)
    """
    All the left children of a node can have a MAX value of the parent node
    All the right children of a node can have a MIN value of the parent node
    """
    if not bintree_node:
        return True    
    
    if bintree_node.value >= min and bintree_node.value <= max:
        if bintree_node.left:
            left_tree_binary =  is_binary_tree(bintree_node.left, min, bintree_node.value)
            if not left_tree_binary:
                return False
        
        if bintree_node.right:
            right_tree_binary = is_binary_tree(bintree_node.right, bintree_node.value, max)
            if not right_tree_binary:
                return False
        
        """
        This block could also be:
        
        if not is_binary_tree(bintree_node.left, min, bintree_node.value) or not is_binary_tree(bintree_node.right, bintree_node.value, max):
            return False
        """
    else:
        return False
    
    return True

if __name__ == "__main__":
    valid_bintree = build_valid_binary_tree()
    invalid_bintree = build_invalid_binary_tree()
    min = -sys.maxint - 1
    max = sys.maxint
    assert is_binary_tree(valid_bintree.root, min, max) == True
    assert is_binary_tree(invalid_bintree.root, min, max) == False
    
    print "All tests passed."