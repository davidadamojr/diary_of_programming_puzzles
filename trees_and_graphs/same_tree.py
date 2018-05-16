"""
Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and 
the nodes have the same value.

https://leetcode.com/problems/same-tree/
"""

from trees import TreeNode


def is_same_tree(first_tree, second_tree):
    if not first_tree and not second_tree:
        return True

    if not first_tree:
        return False

    if not second_tree:
        return False

    if first_tree.value == second_tree.value:
        left_is_equal = is_same_tree(first_tree.left, second_tree.left)
        right_is_equal = is_same_tree(first_tree.right, second_tree.right)

        if left_is_equal and right_is_equal:
            return True

    return False


if __name__ == '__main__':
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)

    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    assert is_same_tree(root1, root2) == True

    root2.right.right = TreeNode(4)
    assert is_same_tree(root1, root2) == False

    print("All test cases passed.")
