class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    
    def __str__(self):
        return str(self.value)

class BinarySearchTree:
    def __init__(self, root):
        self.root = root
        
    def insert(self, key):
        current_node = self.root
        
        while True:
            if key <= current_node.value:
                if current_node.left:
                    current_node = current_node.left
                else:
                    current_node.left = TreeNode(key)
                    break
            else:
                if current_node.right:
                    current_node = current_node.right
                else:
                    current_node.right = TreeNode(key)
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

class BinaryTree:
    def __init__(self, root):
        self.root = root
    
    def __str__(self):
        node_list = []
        queue = [self.root]
        while queue:
            current_node = queue.pop()
            node_list.append(str(current_node))
            if current_node.left:
                queue.insert(0, current_node.left)
            if current_node.right:
                queue.insert(0, current_node.right)
        
        return ",".join(node_list)
