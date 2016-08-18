"""
Write an algorithm to find the "next" node (i.e. in-order successor) of a given 
node in a binary search tree. You may assume that each node has a link to its 
parent.
"""

def in_order_successor(tree_node):
    if tree_node is None:
        return None
    
    if tree_node.right:
        # in order traversal of right subtree - leftmost node of right subtree
        return get_leftmost_node(tree_node.right)
        
    current_node = tree_node
    while current_node.parent and current_node.parent.right == current_node:
        current_node = tree_node.parent
    
    return current_node.parent

def get_leftmost_node(start_node):
    if start_node.left is None:
        return start_node
    
    return get_leftmost_node(start_node.left)
    
    