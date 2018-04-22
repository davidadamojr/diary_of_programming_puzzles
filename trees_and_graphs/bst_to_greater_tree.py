"""
Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed
to the original key plus sum of all keys greater than the original key in BST.

Example:

Input: The root of the Binary Search Tree like this:
        5
       / \
      2  13

Output: The root of a Greater Tree like this:
         18
        /  \
       20  13
"""

from trees import TreeNode

greater_sum = 0


def convert_bst(root):
    if not root:
        return root

    traverse(root)
    return root


def traverse(node):
    global greater_sum
    if node.left is None and node.right is None:
        node.value += greater_sum
        greater_sum = node.value
        return

    if node.right:
        traverse(node.right)

    node.value += greater_sum
    greater_sum = node.value

    if node.left:
        traverse(node.left)

tree_root = TreeNode(5, TreeNode(2), TreeNode(13))
convert_bst(tree_root)
print tree_root
print tree_root.left
print tree_root.right
