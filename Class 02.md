# Array-Insert-Shift
Write a function called insertShiftArray which takes in an array and a value to be added. Without utilizing any of the built-in methods available to your language, return an array with the new value added at the middle ind

## Whiteboard Process
![Whiteboard Picture](https://github.com/houseofjavascript/data-structures-and-algorithms/files/11035868/Untitled.pdf)

## Approach & Efficiency
 I took a very simple approach to divide the list and insert the paremeter by shifting every range in the list? 
I took a 1 to 1 relationship in the big O.

## Solution

def insert_in_middle(my_list, param):
    index = len(my_list) // 2  # index where parameter should be inserted

    # Shift all elements to the right of the index one position to the right
    for i in range(len(my_list) - 1, index - 1, -1):
        my_list[i] = my_list[i - 1]

    # Insert the parameter at the specified index
    my_list[index] = param

    return my_list
