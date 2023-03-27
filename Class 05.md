# Linked-List
Write a function called BinarySearch which takes in 2 parameters: a sorted array and the search key. Without utilizing any of the built-in methods available to your language, return the index of the array’s element that is equal to the value of the search key, or -1 if the element is not in the array.


## Approach & Efficiency

Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node.
Linked List

Create a Linked List class
Within your Linked List class, include a head property.
Upon instantiation, an empty Linked List should be created.
The class should contain the following methods
insert
Arguments: value
Returns: nothing
Adds a new node with that value to the head of the list with an O(1) Time performance.
includes
Arguments: value
Returns: Boolean
Indicates whether that value exists as a Node’s value somewhere within the list.
to string
Arguments: none
Returns: a string representing all the values in the Linked List, formatted as:
"{ a } -> { b } -> { c } -> NULL"

# Return 

this linkedlist can return 
print(my_list.to_string()) # "{ 1 } -> { 2 } -> { 3 } -> NULL"

Allows for communication between the nodes and return information based on the entire list

# Time

This took me 1 hour, thought it would take me 30 minutes
