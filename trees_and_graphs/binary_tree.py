class BinaryTreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    
    def __str__(self):
        return self.value

class BinaryTree:
    def __init__(self, root):
        self.root = root

    def __str__(self):
        queue = [self.root]
        tree_str = ""

        while queue: # while queue is not empty
            current_node = queue.pop()
            tree_str = tree_str + str(current_node) + ","
            if current_node.left:
                queue.insert(0, current_node.left)

            if current_node.right:
                queue.insert(0, current_node.right)

        return tree_str
