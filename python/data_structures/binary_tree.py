class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def pre_order(self):
        def traverse(node, result):
            if node:
                result.append(node.value)
                traverse(node.left, result)
                traverse(node.right, result)

        result = []
        traverse(self.root, result)
        return result

    def in_order(self):
        def traverse(node, result):
            if node:
                traverse(node.left, result)
                result.append(node.value)
                traverse(node.right, result)

        result = []
        traverse(self.root, result)
        return result

    def post_order(self):
        def traverse(node, result):
            if node:
                traverse(node.left, result)
                traverse(node.right, result)
                result.append(node.value)

        result = []
        traverse(self.root, result)
        return result
