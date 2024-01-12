#!/bin/python3

# METHOD 1
'''
The code defines a function `reverseArray` that takes an input list (`arr`) and returns a
new list containing the elements of the input list in reverse order. The approach taken
here is to iterate through the input list in reverse using a `for` loop and append each
element to a new list (`reversed_array`).

### Explanation: ###
1. The loop iterates over the range `len(arr) - 1` to `0` (inclusive) with a step of `-1`,
effectively traversing the input list in reverse order.

2. For each index `i` in the reversed range, the corresponding element at index `i` in the
input list (`arr`) is appended to the `reversed_array`.

### Big O Time Complexity: ###
The time complexity of this approach is `O(n)`, where `n` is the length of the input list (`arr`).
This is because the loop iterates through each element in the input list once, and the time
required for each iteration is constant.

### Big O Space Complexity: ###
The space complexity is also `O(n)` because a new list (`reversed_array`) is created to store the
reversed elements, and its size is directly proportional to the size of the input list.
'''

def reverseArray(arr):
    if isinstance(arr, list):
        reversed_array = []
        for i in range(len(arr) - 1, -1, -1):
            reversed_array.append(arr[i])
        return reversed_array
    raise TypeError(f"ERROR: Argument passed must be of type 'list'")

# Example usage
# Example 1:
my_list1 = [1, 2, 3, 4, 5]
print("Example 1:", reverseArray(my_list1))

# Example 2:
my_list2 = ["apple", "banana", "cherry", "date", "fig", "grape", "kiwi"]
print("Example 2:", reverseArray(my_list2))

# Example 3:
my_list3 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("Example 3:", reverseArray(my_list3))


# METHOD 2
'''
The code defines a function `reverseArray2` that takes an input list (`list`) and reverses its elements
in-place by swapping elements from the beginning and end of the list. The approach taken here is to use
a `for` loop to iterate through half of the list and swap elements.

### Explanation: ###
1. The loop iterates over the range `length // 2`, where `length` is the length of the input list. This
is done to avoid unnecessary swaps since swapping the first half with the second half effectively
reverses the entire list.

2. For each iteration of the loop, the elements at index `i` and `length - 1 - i` are swapped using
tuple unpacking and simultaneous assignment.

### Big O Time Complexity: ###
The time complexity of this approach is O(n), where n is the length of the input list (`list`). The
loop iterates through half of the list, and each iteration involves a constant-time operation (swapping
two elements).

### Big O Space Complexity: ###
The space complexity is O(1), as the algorithm performs the reversal in-place without using any
additional data structures that scale with the input size. The only extra space used is for a few
variables (`length`, `i`), which are constant regardless of the input size.
'''

def reverseArray2(lst):
    if isinstance(lst, list):
        length = len(lst)
        for i in range(length // 2):
            lst[i], lst[length - 1 - i] = lst[length - 1 - i], lst[i]
    else:
        raise TypeError(f"ERROR: Argument passed must be of type 'list'")

# Example usage:
random_strings = ["apple", "banana", "cherry", "date", "fig", "grape", "kiwi"]
my_list = [1, 2, 3, 4, 5]
reverseArray2(random_strings)
print(random_strings)
