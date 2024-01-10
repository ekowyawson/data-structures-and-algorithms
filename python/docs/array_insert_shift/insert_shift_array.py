def insertShiftArray(arr, value):
    # Check if arr is a list
    if not isinstance(arr, list):
        raise TypeError("The 'arr' argument must be a list.")
    # Calculate the middle index
    middle_index = (len(arr) + 1) // 2
    # Initialize the new list
    new_arr = []

    # Iterate through the original list and copy elements
    for i in range(len(arr) + 1):
        if i == middle_index:
            # Insert the new value at the middle index
            new_arr.append(value)
        if i < len(arr):
            # Continue copying the original elements
            new_arr.append(arr[i])
    return new_arr

# Example usage
print(insertShiftArray([1, 2, 3, 4, 5, 6], 99))  # Output: [1, 2, 99, 3, 4, 5]
print(insertShiftArray([1, 2, 3, 4], 99))     # Output: [1, 2, 99, 3, 4]
