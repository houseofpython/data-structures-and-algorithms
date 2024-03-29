# Insertion Sort 

Insertion sort is a simple sorting algorithm that works by repeatedly iterating through an array, comparing each element with the ones before it, and inserting it into the correct position. The algorithm starts by assuming that the first element of the array is sorted. Then, it proceeds to compare the second element with the first one and inserts it into the correct position. It continues this process with each subsequent element until the entire array is sorted. This algorithm has a worst-case time complexity of O(n^2), but it can be efficient for small arrays or partially sorted arrays.

# Example List

[8,4,23,42,16,15]

In the image below we can visually represent how the insertion sort works. We start by comparing the second and first element in an array or list by looking for the lower value and then shifting. In the images the yellow will represent the value that will be compared. This value will turn green when the the value next to it is no longer greater . 

![image](https://github.com/houseofpython/data-structures-and-algorithms/blob/5acb614c4ec8f30d0dd003cb593c2616ace0f1a9/cc-26.jpg)

#Code for how this process works 

```
def insertion_sort(arr):
    # iterate over the array, starting from the second element
    for i in range(1, len(arr)):
        # save the current element so we can insert it in the correct position later
        current = arr[i]
        # start comparing the current element with the ones before it, starting with the one immediately before it
        j = i - 1
        # while the element before the current one is greater than the current one, shift the element before the current one to the right
        while j >= 0 and arr[j] > current:
            arr[j + 1] = arr[j]
            j -= 1
        # insert the current element in the correct position
        arr[j + 1] = current
    # return the sorted array
    return arr
```
# Summary 

- Insertion sort is a sorting algorithm that builds the final sorted array one item at a time.
- It starts by assuming that the first element of the array is already sorted.
- For each subsequent element, it inserts it into the correct position in the sorted part of the array.
- To do this, it compares the current element to the ones before it and shifts them over if they are greater.
- Once it finds the correct position for the current element, it inserts it there and moves on to the next element.
- Insertion sort has a worst-case time complexity of O(n^2), making it inefficient for large arrays.
- However, it has a best-case time complexity of O(n), which makes it a good choice for small arrays or arrays that are already partially sorted.
- Insertion sort is an in-place sorting algorithm, meaning it sorts the array in place without requiring additional memory.

# If we wanted to test this implementation we could use the following :
```
import unittest

class TestInsertionSort(unittest.TestCase):
    def test_sort(self):
        arr = [8, 4, 23, 42, 16, 15]
        expected = [4, 8, 15, 16, 23, 42]
        result = insertion_sort(arr)
        self.assertEqual(result, expected)
```
