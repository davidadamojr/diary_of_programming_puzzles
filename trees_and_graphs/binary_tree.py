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
        
    def insert(self, key):
        current_node = self.root
        
        while True:
            if key <= current_node.value:
                if current_node.left:
                    current_node = current_node.left
                else:
                    current_node.left = BinaryTreeNode(key)
                    break
            else:
                if current_node.right:
                    current_node = current_node.right
                else:
                    current_node.right = BinaryTreeNode(key)
                    break
                

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
