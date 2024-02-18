# Code Challenge 32: Find Common Values in Two Binary Trees

## Problem Domain

Write a function that takes **two binary trees** as parameters that uses a **hash-map** to return a set of values found in both trees. The function/s must utilize the **Single-responsibility** principle (*any methods you write should be clean, reusable, abstract component parts to the whole*).

[Link to code](../../code_challenges/tree_intersection.py)

## Collaborators

> Stephanie Johnson
> Latherio Kidd

## Whiteboard Process

N/A

## Approach & Efficiency

For the `tree_intersection` function, I utilized the `Hashtable` class to efficiently identify intersecting values between two binary trees. The function traverses each tree once, using the hashtable to track values seen in the first tree and then to identify which of those values also appear in the second tree. This strategy leverages the hashtable's efficient data retrieval capabilities to minimize the time required to find intersections.

### Big O Space/Time Complexity

- **Time Complexity**:
  - The overall time complexity of the `tree_intersection` function is `O(n + m)`, where `n` is the number of nodes in the first tree and `m` is the number of nodes in the second tree. This complexity arises because each tree is traversed in full once. The time complexity for the hashtable operations (`set` and `has`) is `O(1)` on average, contributing minimally to the total time complexity.
- **Space Complexity**:
  - The space complexity is `O(n + k)`, where `n` is the number of unique values in the first tree and `k` is the number of intersecting values found in both trees. The `n` part comes from storing each value of the first tree in the hashtable, and `k` represents the space needed to store the intersecting values in the output set.

## Solution

1. **Input**: Two binary trees with overlapping and unique values.
   - Process: Traverse the first tree and store its values in a hashtable. Then, traverse the second tree, checking for each value if it exists in the hashtable, indicating an intersection.
   - Output: A set of values found in both trees.

2. **Example Usage**:

```python
# Assume tree1 and tree2 are previously defined binary trees with integer values.
intersecting_values = tree_intersection(tree1, tree2)
print(intersecting_values)  # Expected output: A set of integers that are present in both trees.
```

### Example Scenario

- **Given Trees**:
  - Tree 1 contains the values [1, 2, 3, 4, 5].
  - Tree 2 contains the values [4, 5, 6, 7, 8].
- **Process**: The `tree_intersection` function first stores the values of Tree 1 in a hashtable. It then checks the values of Tree 2 against this hashtable.
- **Output**: The function returns the set `{4, 5}`, which represents the intersection of values between the two trees.

### Checklist

- [x] Top-level README “Table of Contents” is updated
- [x] README for this challenge is complete
  - [x] Summary, Description, Approach & Efficiency, Solution
  - [x] Picture of whiteboard
  - [x] Link to code
- [x] Feature tasks for this challenge are completed
- [x] Unit tests written and passing
  - [x] “Happy Path” - Expected outcome
  - [x] Expected failure
  - [x] Edge Case (if applicable/obvious)
