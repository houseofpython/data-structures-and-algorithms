# Stack-Queue-Brackets

Write a function called validate brackets
Arguments: string
Return: boolean
representing whether or not the brackets in the string are balanced
There are 3 types of brackets:

Round Brackets : ()
Square Brackets : []
Curly Brackets : {}


## Whiteboard Process
![Whiteboard Picture](https://github.com/houseofjavascript/data-structures-and-algorithms/files/11035868/Untitled.pdf)

## Approach & Efficiency

Use a stack to store and compare closing parameters

Big O 1n for time
BIG O On for space


## Solution


open_list = ["[","{","("]
close_list = ["]","}",")"]

def check(mystring):
    stack = []
    for i in mystring:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if ((len(stack) > 0) and
                (open_list[pos] == stack[len(stack)-1])):
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    else:
        return False

