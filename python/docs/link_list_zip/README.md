# Code Challenge 06: Linked List k-th value from the end

In this **linked list** challenge, we extend a Linked List to allow `kth from end` methods.

[Link to code](./linked_list_kth/linked_list_kth.py)

## Whiteboard Process

N/A - Diagram not needed for such a change

## Approach & Efficiency

In the implementation of the `kth_from_end` method for the `LinkedList` class, I took a straightforward, two-pass approach. Here's a breakdown of the rationale and the Big O space and time complexity analysis:

### Approach Taken

#### Input Validation

First, the method checks if `k` is a non-negative integer, raising a `TargetError` for invalid inputs. This is a basic error handling practice to ensure that the method receives appropriate arguments.

#### Count Total Nodes

The method traverses the entire linked list to count the total number of nodes. This step is necessary to determine the list's length and validate if `k` is within range.

#### Calculate Target Position

After knowing the total number of nodes, it calculates the position of the kth node from the beginning, which is `total_nodes - k`.

#### Traverse to Target Node

Finally, the method traverses the list again to reach the calculated position and returns the value of that node.

### Why This Approach?

- **Simplicity and Clarity**: This approach is straightforward and easy to understand, making the code more maintainable and clear.

- **No Extra Data Structures**: It doesn't require any additional data structures, keeping the space complexity minimal.

- **Single Responsibility**: Each step of the method has a clear purpose, adhering to the principle of single responsibility.

### Big O Space/Time Complexity

- **Time Complexity**: *O(N)*
  - The first pass to count the nodes is O(N), where N is the number of nodes in the list.
  - The second pass to reach the target node is also O(N) in the worst case (when `k` is 0, and we traverse the entire list again).
  - Therefore, the total time complexity is O(N) + O(N) ≈ O(N).

- **Space Complexity**: *O(1)*
  - No extra space is used proportional to the input size. Only a fixed number of variables (`current`, `total_nodes`, `target_position`) are used, irrespective of the size of the input linked list.
  - This makes the space complexity constant, O(1).

This approach is a balanced choice considering the simplicity of implementation and the constraints of the problem. It's particularly suitable for scenarios where space efficiency is crucial and a slight trade-off in time complexity is acceptable.

## Solution

To run the code, you would do the following:

1. Instantiate a `LinkedList` object by assigning it to a variable:`linked_list = LinkedList()`.
2. Add values to the linked list instance by calling the `insert` method: `linked_list.insert(1)`.
3. Check to see if the list contains a value by calling the `includes` method: `linked_list.includes(24)`.
4. Insert a new node after an existing value by calling the `insert_after` method passing the existing value and the new value.
5. Insert a new node before an existing value by calling the `insert_after` method passing the existing value and the new value.
6. Append a new node by calling the `append` method and passing in the value of the new node.

### Example Usage

Input:

```python
# Example usage of the LinkedList class
linked_list = LinkedList()
linked_list.insert(3)
linked_list.insert(2)
linked_list.insert(1)
linked_list.append(10)
linked_list.insert_before(10, 5)
linked_list.insert_after(10, 15)
linked_list.insert_after(15, 25)

print("Linked List:", linked_list.to_string())
print("Includes 2:", linked_list.includes(2))
print("Includes 4:", linked_list.includes(4))
```

Example usage of `kth`:

```python
# Example usage of the LinkedList class
# Assuming the LinkedList and Node classes are already defined,
# as well as the kth_from_end method within the LinkedList class.

# Create an instance of LinkedList
linked_list = LinkedList()

# Add some values to the list
values_to_add = ["node1", "node2", "node3", "node4", "node5"]
for value in reversed(values_to_add):
    linked_list.insert(value)

# Now, let's use the kth_from_end method
try:
    # Get the value of the node that is 2 places from the end of the list
    value_at_k = linked_list.kth_from_end(2)
    print(f"The value of the node 2 places from the end is: {value_at_k}")

    # You can also try other values of k
    # For example, to get the last node
    last_node_value = linked_list.kth_from_end(0)
    print(f"The value of the last node is: {last_node_value}")

except ValueError as e:
    print(f"Error: {e}")

```

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
