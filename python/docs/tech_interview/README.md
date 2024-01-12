# Code Challenge: Technical Interview

Placeholder

[Link to code](./list_reverse.py)

## Whiteboard Process

![White Board](White_Board.png)

## Approach & Efficiency

Placeholder

### Explanation:

Placeholder

### Big O Time Complexity:

Placeholder

### Big O Space Complexity:

Placeholder

## Solution

To run the code, you would first define a list variable, then pass that variable as a parameter to
the `reverseArray` function.

Examples:

```python
def reverseArray(arr):
    if isinstance(arr, list):
        reversed_array = []
        for i in range(len(arr) - 1, -1, -1):
            reversed_array.append(arr[i])
        return reversed_array
    raise TypeError(f"ERROR: Argument passed must be of type 'list'")

# Example 1:
my_list1 = [1, 2, 3, 4, 5]
print("Example 1:", reverseArray(my_list1))

# Example 2:
my_list2 = ["apple", "banana", "cherry", "date", "fig", "grape", "kiwi"]
print("Example 2:", reverseArray(my_list2))

# Example 3:
my_list3 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("Example 3:", reverseArray(my_list3))
```

Output:

```bash
python3 list_reverse.py
Example 1: [5, 4, 3, 2, 1]
Example 2: ['kiwi', 'grape', 'fig', 'date', 'cherry', 'banana', 'apple']
Example 3: [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
```

- [x] Top-level README “Table of Contents” is updated
- [x] README for this challenge is complete
  - Summary, Description, Approach & Efficiency, Solution
  - Picture of whiteboard
  - Link to code
- [x] Feature tasks for this challenge are completed
- [ ] Unit tests written and passing
  - [ ] “Happy Path” - Expected outcome
  - [ ] Expected failure
  - [ ] Edge Case (if applicable/obvious)
