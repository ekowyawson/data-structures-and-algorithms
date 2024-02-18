# Code Challenge 30: Hash Table Implementation

## Problem Domain

Design and implement a `Hashtable` class in Python that efficiently manages **key-value pairs**. The class should offer functionality to `add`, `retrieve`, and `check` the existence of keys in the hashtable, as well as `list` all stored keys. It must also handle collisions gracefully and allow for the replacement of values associated with existing keys.

[Link to code](../../data_structures/hashtable.py)

## Whiteboard Process

N/A

## Approach & Efficiency

For the `Hashtable` class, I implemented it with an array of `buckets`, where each bucket is a list that stored key-value pairs. This structure allows for efficient data retrieval, insertion, and management by using a hash function to map keys to indices in the array, thus determining the location of the data in the hashtable. Handling collisions (where different keys produce the same hash value) is done through chaining, by storing colliding elements in the same bucket as a linked list. This method ensures that all elements can be stored and retrieved even when hashes collide.

### Big O Space/Time Complexity

- **Time Complexity**:
  - `set`, `get`, and `has` methods: `O(1)` average and `O(n)` worst-case.
    - In the average case, these operations perform very efficiently due to direct indexing by hash values.
    - The worst-case scenario occurs when many keys hash to the same value, resulting in a long chain that must be iterated through.
  - `keys` method: `O(n)`, as it needs to iterate through all buckets and the chains within them to collect all keys.

- **Space Complexity**: `O(n)`
  - The space complexity is linear with respect to the number of key-value pairs stored in the hashtable. While the hashtable itself has a fixed size, the space required grows with the number of elements due to the storage of actual data in the buckets.

## Solution

1. **Input**: `set("name", "John")`, `set("age", "30")`, `set("city", "New York")`
   - Process: Store each key-value pair in the hashtable, using the hash function to determine the bucket index.
   - Output: The hashtable stores the key-value pairs, handling any potential collisions.

2. **Input**: `get("name")`
   - Process: Retrieve the value associated with the key `"name"`.
   - Output: `"John"` (demonstrates successful retrieval from the hashtable)

3. **Input**: `has("city")`
   - Process: Check if the key `"city"` exists in the hashtable.
   - Output: `True` (indicates the presence of the key)

4. **Input**: `keys()`
   - Process: List all keys stored in the hashtable.
   - Output: `["name", "age", "city"]` (or similar, depending on the order in the internal structure)

### Example Usage

```python
hashtable = Hashtable()
hashtable.set("name", "John")
hashtable.set("age", "30")
hashtable.set("city", "New York")

print(hashtable.get("name"))  # Expected "John"
print(hashtable.get("age"))   # Expected "30"
print(hashtable.get("city"))  # Expected "New York"
print(hashtable.has("name"))  # Expected True
print(hashtable.has("country"))  # Expected False
print(hashtable.keys())  # Expected ["name", "age", "city"]
```

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
