class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

def zip_lists(list1, list2):
    if list1 is None:
        return list2
    if list2 is None:
        return list1
    new_list = LinkedList()
    current1 = list1.head
    current2 = list2.head
    while current1 is not None and current2 is not None:
        new_list.add_node(current1.data)
        new_list.add_node(current2.data)
        current1 = current1.next
        current2 = current2.next
    if current1 is not None:
        new_list.add_node(current1.data)
    if current2 is not None:
        new_list.add_node(current2.data)
    return new_list
