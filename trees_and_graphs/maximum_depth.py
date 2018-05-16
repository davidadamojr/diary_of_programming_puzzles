"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root 
node down to the farthest leaf node.
"""

from trees import TreeNode
from trees import BinaryTree


def maximum_depth(node):
    if not node:
        return 0

    return 1 + max(maximum_depth(node.left), maximum_depth(node.right))


if __name__ == '__main__':
    root_node = TreeNode(10)
    root_node.left = TreeNode(12)
    root_node.right = TreeNode(24)
    root_node.left.left = TreeNode(1)
    root_node.left.left.left = TreeNode(1)
    binary_tree = BinaryTree(root_node)

    assert maximum_depth(binary_tree.root) == 4
    print("All test cases passed.")
