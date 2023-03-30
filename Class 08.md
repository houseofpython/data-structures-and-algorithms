
# Linked-List-Zip 
Write a function called zip lists
Arguments: 2 linked lists
Return: New Linked List, zipped as noted below
Zip the two linked lists together into one so that the nodes alternate between the two lists and return a reference to the the zipped list.
Try and keep additional space down to O(1)
You have access to the Node class and all the properties on the Linked List class as well as the methods created in previous challenges.


## Whiteboard Process
![Whiteboard Picture](https://github.com/houseofjavascript/data-structures-and-algorithms/files/11035868/Untitled.pdf)

## Approach & Efficiency

Use a while loop to run through both list as longer as neither is none. Each iteration we add a node to the newly created list. Once they are added we move the pionters to the next nodes.

Big O is On
Big O is 2n


## Solution


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





