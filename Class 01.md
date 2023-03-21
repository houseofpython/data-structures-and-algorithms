# Challenge Title
Take in an list and output the list in reverse 

## Whiteboard Process
 [Class 01](https://houseofjavascript.github.io/reading-notes/class%2001)

## Approach & Efficiency
Simply remove each item from the array using a formula and pushed it into a new array using -x. Time -> 0(n) Because this is a 1 to 1 relationship, that growing proportional to the original List
Space -> 0(2n) for every one item added to the list it will take 1 action to complete 

## Solution
def reverse_list(items):
  if type(items) is not list:
    return "not a list"
  else:
    new_list = []
    for x in range(len(items)):
        new_list.append(items[-(x+1)])
        print(new_list)
    return new_list
