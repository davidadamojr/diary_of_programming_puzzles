"""
Given a binary tree, design an algorithm which creates a linked list of all 
the nodes at each depth (e.g. if you have a tree with depth D, you'll have 
D linked lists)
"""

import sys

sys.path.insert(0, '../linked_lists')
sys.path.insert(0, '../trees_and_graphs')

from linked_list import LinkedListNode
from trees import *

# build binary tree
root_node = TreeNode(1)
tree = BinaryTree(root_node)
queue = [root_node]
node_value = 2
while queue:
    node = queue.pop()

    node.left = TreeNode(node_value)
    queue.insert(0, node.left)
    node_value = node_value + 1

    node.right = TreeNode(node_value)
    queue.insert(0, node.right)
    if node_value == 15:
        break
    node_value = node_value + 1


def create_list(tree):
    queue = [tree.root]
    level = 0
    list_of_lists = []
    while queue:
        head = LinkedListNode(queue[0].value)
        current_node = head
        children = []
        if queue[0].left: children.append(queue[0].left)
        if queue[0].right: children.append(queue[0].right)
        for node in queue[1:]:
            current_node.next = LinkedListNode(node.value)
            current_node = current_node.next
            if node.left:
                children.append(node.left)
            if node.right:
                children.append(node.right)
        list_of_lists.append(head)
        queue = children

    return list_of_lists


if __name__ == '__main__':
    list_levels = create_list(tree)
    for linked_list in list_levels:
        print(linked_list)
