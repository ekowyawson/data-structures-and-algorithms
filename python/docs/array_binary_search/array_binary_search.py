#!/bin/python3

def BinarySearch(sorted_array, search_key):
   """
   Performs a binary search on a sorted array to find the index of the search key.

   Args:
       sorted_array: A sorted list of elements.
       search_key: The value to search for in the array.

   Returns:
       The index of the first occurrence of the search key in the array, or -1 if not found.
   """
   low = 0
   high = len(sorted_array) - 1

   while low <= high:
       mid = (low + high) // 2
       if sorted_array[mid] == search_key:
           return mid
       elif sorted_array[mid] < search_key:
           low = mid + 1
       else:
           high = mid - 1
   return -1


# Example 1:
sorted_array = [4, 8, 15, 16, 23, 42]
search_key = 15
result = BinarySearch(sorted_array, search_key)
print("Index of 15 in the array:", result)

# Example 2:
sorted_array = [-131, -82, 0, 27, 42, 68, 179]
search_key = 42
result = BinarySearch(sorted_array, search_key)
print("Index of 42 in the array:", result)

# Example 3: (Searching for a value not in the array)
sorted_array = [-131, -82, 0, 27, 42, 68, 179]
search_key = 100
result = BinarySearch(sorted_array, search_key)
print("Index of 100 in the array:", result)  # Output: Index of 100 in the array: -1
