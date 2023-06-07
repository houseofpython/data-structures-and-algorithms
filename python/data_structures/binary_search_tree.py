from data_structures.binary_tree import BinaryTree
from data_structures.binary_tree import Node

class BinarySearchTree(BinaryTree):
    def __init__(self):
        super().__init__()

    def add(self, value):
        def insert(node, value):
            if value < node.value:
                if node.left is None:
                    node.left = Node(value)
                else:
                    insert(node.left, value)
            else:
                if node.right is None:
                    node.right = Node(value)
                else:
                    insert(node.right, value)

        if self.root is None:
            self.root = Node(value)
        else:
            insert(self.root, value)

    def contains(self, value):
        def search(node, value):
            if node is None:
                return False
            elif node.value == value:
                return True
            elif value < node.value:
                return search(node.left, value)
            else:
                return search(node.right, value)

        return search(self.root, value)
