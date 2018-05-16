"""
Given a directed graph, design an algorithm to find out whether there is a route 
between two nodes.
"""


class Node:
    def __init__(self, label):
        self.neighbors = []
        self.label = label
        self.visited = False


# @param start_node starting node in path to be found
# @param end_node ending node in path to be found
# @param return boolean true if there is path, false if there is not
def find_path(start_node, end_node):
    """
    This requires a simple graph traversal using either depth-first search 
    or breadth-first search. Breadth-first search is likely to be quicker and 
    is likely to provide the shortest path.
    """
    queue = [start_node]
    while queue != []:
        current_node = queue.pop()
        current_node.visited = True
        if current_node == end_node:
            return True

        for neighbor in current_node.neighbors:
            if not neighbor.visited:
                queue.insert(0, neighbor)

    return False


a_node = Node("a")
b_node = Node("b")
c_node = Node("c")
d_node = Node("d")
e_node = Node("e")
f_node = Node("f")

a_node.neighbors.extend([b_node, c_node])
b_node.neighbors.extend([c_node, d_node])
c_node.neighbors.extend([d_node])
d_node.neighbors.extend([a_node])
e_node.neighbors.extend([c_node, f_node])
f_node.neighbors.extend([b_node])

print(find_path(a_node, d_node))  # return true
print(find_path(a_node, f_node))  # return false
