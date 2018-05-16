class LinkedListNode:
    def __init__(self, data):
        self.next = None
        self.data = data

    def __str__(self):
        node_str = ""
        current_node = self
        while current_node:
            if current_node.next:
                node_str = node_str + str(current_node.data) + ", "
            else:
                node_str = node_str + str(current_node.data)

            current_node = current_node.next

        return node_str
