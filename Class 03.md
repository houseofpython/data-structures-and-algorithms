# Array-Insert-Shift
Write a function called BinarySearch which takes in 2 parameters: a sorted array and the search key. Without utilizing any of the built-in methods available to your language, return the index of the array’s element that is equal to the value of the search key, or -1 if the element is not in the array.

## Whiteboard Process
![Whiteboard Picture](https://github.com/houseofjavascript/data-structures-and-algorithms/blob/09c9e5e73ae6d64e0a2a18e1ca4005aa7da898a7/Class%2003%20Code%20Challenge.pdf)


## Approach & Efficiency

Use a binary search method thorugh python to iterate through the list left to right and then right to left until finding the match and then returned the index.


## Solution

def binary_search(arr, search_key):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == search_key:
            return mid
        elif arr[mid] < search_key:
            left = mid + 1
        else:
            right = mid - 1
    return -1
code-fellows
raised_hands
heavy_plus_sign





3:28
arr = [1, 3, 5, 7, 9, 11]
search_key = 7
index = binary_search(arr, search_key)
print(index)  # Output: 3
