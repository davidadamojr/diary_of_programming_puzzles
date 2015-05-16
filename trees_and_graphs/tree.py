class Tree:
    def __init__(self, value, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value

    def __str__(self):
        queue = [self]
        tree_str = ""

        while len(queue) != 0:
            current_node = queue.pop()
            tree_str = tree_str + str(current_node.value) + ","
            if current_node.left:
                queue.insert(0, current_node.left)

            if current_node.right:
                queue.insert(0, current_node.right)

        return tree_str
