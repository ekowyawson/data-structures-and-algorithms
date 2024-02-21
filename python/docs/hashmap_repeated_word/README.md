# Code Challenge 31: Hashmap Repeated Word

## Problem Domain

The task involves developing an algorithm to identify the first word in a given text that appears more than once.
This problem domain is crucial for applications in text analysis, natural language processing, and similar fields
where processing and understanding textual data is required.

[Link to code](../../code_challenges/hashtable_repeated_word.py)

## Collaborators

> Stephanie Johnson
> Latherio Kidd

## Whiteboard Process

N/A

## Approach & Efficiency

For the `first_repeated_word` function, the approach involves iterating through the words in a given string, processing each word to normalize its format by removing punctuation at the start and end, and converting it to lowercase. This standardization allows for case-insensitive comparison and ensures that words connected to punctuation are treated as separate entities. The processed words are then checked against a set that keeps track of words that have already been seen. This method efficiently identifies the first repeated word by leveraging the quick lookup capabilities of a set in Python.

### Big O Space/Time Complexity

- **Time Complexity**:
  - The overall time complexity of the function is `O(n)`, where `n` is the number of words in the input string. This accounts for splitting the string into words and iterating through them. The operation to strip punctuation and convert to lowercase is considered constant time, `O(1)`, for each word, as the length of the words is typically much smaller than the length of the entire string. The set operation for checking and adding words also operates in average case constant time, `O(1)`.

- **Space Complexity**:
  - The space complexity is `O(m)`, where `m` is the number of unique words in the input string. This is due to the storage requirement for the set that tracks words already seen. In the worst case, if all words are unique, the space required grows linearly with the number of words.

## Solution

1. **Input**: A paragraph of text with potential repeated words, interspersed with punctuation.
   - Process: The text is split into words, each word is cleaned of leading and trailing punctuation and converted to lowercase, and then each word is checked against a set of seen words to find the first repetition.
   - Output:  The first word found to be repeated in the text, or None if there are no repeated words.

### Example Usage

```python
first_repeated_word("apple? BANANA! banana, apple.")

#Output:
# banana
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
