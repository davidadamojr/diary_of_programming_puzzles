"""
Find the sum of left leaves in a given binary tree.

Example:
            3
           / \
          9  20
            /  \
           15  7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.

https://leetcode.com/problems/sum-of-left-leaves/
"""

from trees import TreeNode


def sum_of_left_leaves(root):
    if not root:
        return 0

    if root.left and not root.left.left and not root.left.right:
        return root.left.value + sum_of_left_leaves(root.right)

    return sum_of_left_leaves(root.left) + sum_of_left_leaves(root.right)


if __name__ == "__main__":
    root1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert sum_of_left_leaves(root1) == 24

    root2 = TreeNode(3)
    assert sum_of_left_leaves(root2) == 0

    root3 = TreeNode(3, TreeNode(9), TreeNode(20))
    assert sum_of_left_leaves(root3) == 9

    root4 = TreeNode(3, TreeNode(9, TreeNode(10), TreeNode(11)), TreeNode(20, TreeNode(15), TreeNode(17)))

    print("All test cases passed successfully")
