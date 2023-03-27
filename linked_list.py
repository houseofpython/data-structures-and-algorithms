

class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        new_node.next_node = self.head
        self.head = new_node

    def includes(self, value):
        current_node = self.head
        while current_node:
            if current_node.value == value:
                return True
            current_node = current_node.next_node
        return False

    def to_string(self):
        current_node = self.head
        output = ""
        while current_node:
            output += "{ " + str(current_node.value) + " } -> "
            current_node = current_node.next_node
        output += "NULL"
        return output


