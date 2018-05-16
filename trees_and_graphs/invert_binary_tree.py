"""
Invert a binary tree.

         4                        4
      /    \                    /   \
    2       7                  7     2 
   /  \   /  \                / \   / \
  1    3 6    9              9   6 3   1
  
"""

from trees import TreeNode, BinaryTree


def invert_binary_tree(tree):
    if not tree:
        return tree

    node_queue = [tree.root]

    while node_queue:
        current_node = node_queue.pop()
        if current_node.left or current_node.right:
            current_node.left, current_node.right = current_node.right, current_node.left

        if current_node.right:
            node_queue.insert(0, current_node.right)

        if current_node.left:
            node_queue.insert(0, current_node.left)

    return tree


if __name__ == '__main__':
    root = TreeNode(4, TreeNode(2), TreeNode(7))
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)
    binary_tree = BinaryTree(root)
    print("Before inversion: ", binary_tree)
    inverted_tree = invert_binary_tree(binary_tree)
    print("After inversion: ", inverted_tree)
