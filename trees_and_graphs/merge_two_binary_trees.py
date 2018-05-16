"""
Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees
are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values as
the new value of the merged node. Otherwise, the NOT null node will be used as the node of the new tree.

Example:
Input:

        Tree 1                          Tree 2
           1                              2
          / \                            / \
        3    2                          1   3
       /                                 \   \
      5                                   4   7

Output:
Merged tree:
        3
       / \
      4   5
     / \   \
    5  4   7

Note: The merging process must start from the root nodes of both trees.

https://leetcode.com/problems/merge-two-binary-trees/description/
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def merge_trees(t1, t2):
    if not t1 and not t2:
        return None

    if not t1:
        return t2

    if not t2:
        return 1

    merged_tree = TreeNode(t1.val + t2.val)
    current_merged_node = merged_tree

    depth_first(t1, t2, current_merged_node)

    return merged_tree


def depth_first(current_t1_node, current_t2_node, current_merged_node):
    t1_left = current_t1_node.left
    t1_right = current_t1_node.right
    t2_left = current_t2_node.left
    t2_right = current_t2_node.right

    if t1_left and t2_left:
        merged_val = t1_left.val + t2_left.val
        merged_node = TreeNode(merged_val)
        current_merged_node.left = merged_node
        depth_first(t1_left, t2_left, merged_node)
    elif t1_left and not t2_left:
        current_merged_node.left = t1_left
    elif not t1_left and t2_left:
        current_merged_node.left = t2_left

    if t1_right and t2_right:
        merged_val = t1_right.val + t2_right.val
        merged_node = TreeNode(merged_val)
        current_merged_node.right = merged_node
        depth_first(t1_right, t2_right, merged_node)
    elif t1_right and not t2_right:
        current_merged_node.right = t1_right
    elif not t1_right and t2_right:
        current_merged_node.right = t2_right


if __name__ == '__main__':
    tree1 = TreeNode(1)
    tree1.right = TreeNode(2)
    tree2 = TreeNode(2)
    tree2.left = TreeNode(5)
    merged_binary_tree = merge_trees(tree1, tree2)
    assert merged_binary_tree.val == 3
    assert merged_binary_tree.right.val == 2
    assert merged_binary_tree.left.val == 5
    print("Test cases passed successfully.")
