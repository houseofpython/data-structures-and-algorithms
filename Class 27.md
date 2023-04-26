# Merge Sort

Merge sort is a popular sorting algorithm that uses a divide-and-conquer approach to sort a list or an array of elements. It works by dividing the input list into smaller halves, sorting each half recursively, and then merging the sorted halves back together

# Let's look at some Pseudo Code 

```
ALGORITHM Mergesort(arr)
    DECLARE n <-- arr.length

    if n > 1
      DECLARE mid <-- n/2
      DECLARE left <-- arr[0...mid]
      DECLARE right <-- arr[mid...n]
      // sort the left side
      Mergesort(left)
      // sort the right side
      Mergesort(right)
      // merge the sorted left and right sides together
      Merge(left, right, arr)

ALGORITHM Merge(left, right, arr)
    DECLARE i <-- 0
    DECLARE j <-- 0
    DECLARE k <-- 0

    while i < left.length && j < right.length
        if left[i] <= right[j]
            arr[k] <-- left[i]
            i <-- i + 1
        else
            arr[k] <-- right[j]
            j <-- j + 1

        k <-- k + 1

    if i = left.length
       set remaining entries in arr to remaining values in right
    else
       set remaining entries in arr to remaining values in left
```

# Let's look at some steps 

- Define a function merge_sort(lst) that takes an unsorted list as input.
- If the length of the list is less than or equal to 1, return the list as it is already sorted.
- Otherwise, split the list into two halves: left_half and right_half.
- Call merge_sort() recursively on both halves to sort them.
- Merge the sorted halves back together into a single sorted list using a merge() function.
- Return the sorted list.

# Now lets look at a sample visual to break this down even further :

![](https://github.com/houseofpython/data-structures-and-algorithms/blob/1dd9adbcf9e0f7c21b403a2634331e306ec6674d/Merge-Sort-Algorithm.png)

# How this code outs in Python : 

```
def merge_sort(lst):
    # If the length of the list is less than or equal to 1, return the list as it is already sorted.
    if len(lst) <= 1:
        return lst
    
    # Divide the list into two halves.
    mid = len(lst) // 2
    left_half = lst[:mid]
    right_half = lst[mid:]
    
    # Recursively sort the left and right halves.
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    # Merge the sorted halves back together into a single sorted list.
    return merge(left_half, right_half)

def merge(left_half, right_half):
    result = []
    i = j = 0
    
    # While there are still elements in both halves, compare the first elements and add the smaller one to the result list.
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            result.append(left_half[i])
            i += 1
        else:
            result.append(right_half[j])
            j += 1
    
    # Add the remaining elements of whichever half still has elements left to the result list.
    result += left_half[i:]
    result += right_half[j:]
    
    # Return the merged, sorted list.
    return result

```
# Try It Yourself 

[8,4,23,42,16,15], using our visual and code can you figure out what this returns ?

```
input_array = [8, 4, 23, 42, 16, 15]
print("Input Array:", input_array)
```

# Summary 

In this conversation, we discussed how merge sort works in Python. Merge sort is a popular sorting algorithm that uses a divide-and-conquer approach to sort a list or an array of elements. It works by dividing the input list into smaller halves, sorting each half recursively, and then merging the sorted halves back together. We looked at the steps involved in implementing the merge sort algorithm in Python and added comments to each line of code to explain what it does. Overall, we learned how to use merge sort to sort a list in Python and gained a better understanding of how the algorithm works


```
sorted_array = merge_sort(input_array)
print("Sorted Array:", sorted_array)
```

# Returned Example 

```
Input Array: [8, 4, 23, 42, 16, 15]
Sorted Array: [4, 8, 15, 16, 23, 42]
```
