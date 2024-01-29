# Binary Search Trees

## Introduction

A Binary Search Tree (**BST**) is a special type of binary tree in which the **left child** of a node has a value ***less than*** the node’s
value and the **right child** has a value ***greater than*** the node’s value. This property is called the **BST** **property** and it makes it
possible to efficiently *search*, *insert*, and *delete* elements in the tree.

The **root** of a **BST** is the node that has *the smallest value in the left subtree* and *the largest value in the right subtree*. Each left
subtree is a **BST** with nodes that have smaller values than the root and each right subtree is a **BST** with nodes that have larger values than
the root.

A **Binary Search Tree** is a node-based binary tree data structure that has the following properties:

- The left subtree of a node contains only nodes with keys lesser than the node’s key.
- The right subtree of a node contains only nodes with keys greater than the node’s key.
  - This means everything to the left of the root is less than the value of the root and everything to the right of the root is greater than the
    value of the root. Due to this performing, a binary search is very easy.
- The left and right subtree each must also be a binary search tree.
- There must be **no duplicate nodes**(**BST** may have duplicate values with different handling approaches)

## Handling Duplicate Values in a Binary Search Tree:

Duplicate values must:

- Follow a consistent process throughout:
  - Either store the duplicate value at the left or store the duplicate value at the right of the root, but be consistent with your approach.
- Keep a counter with the nodes.
  - If a duplicate value occurs, increment the counter.

## BST Operations

### Insert a node into a BST

A new key is always inserted at the leaf. Start searching a key from the root till a leaf node. Once a leaf node is found, the new node is added
as a child of the leaf node.

- **Time Complexity**: **`O(N)`**, where `N` is the number of nodes of the BST
- **Space Complexity**: **`O(1)`**

```python
# Python program to insert a node in a BST
# Create Node class
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Function to insert a new node with given key in BST
def insert(node, key):
    # If the tree is empty, return a new node
    if node is None:
        return Node(key)
    # Otherwise, recur down the tree
    if key < node.key:
        node.left = insert(node.left, key)
    elif key > node.key:
        node.right = insert(node.right, key)

    # Return the node pointer
    return node

# Function to do inorder traversal of BST
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)

if __name__ == '__main__':
    """
    Let us create following BST
          50
       /     \
      30      70
     /  \    /  \
    20  40  60   80
    """
    root = None
    # Inserting value 50
    root = insert(root, 50)
    # Inserting value 30
    insert(root, 30)
    # Inserting value 20
    insert(root, 20)
    # Inserting value 40
    insert(root, 40)
    # Inserting value 70
    insert(root, 70)
    # Inserting value 60
    insert(root, 60)
    # Inserting value 80
    insert(root, 80)
    # Print the BST
    inorder(root)

# OUTPUT:
# 20 30 40 50 60 70 80
```

### Inorder traversal

In case of BSTs, **inorder** traversal traverses nodes in a ***non-decreasing*** order.
We visit the ***left child first***, ***then the root***, and lastly ***the right child***.

**Time Complexity**: `O(N)`, where `N` is the number of nodes of the BST
**Space Complexity**: `O(1)`

```python
# Inorder traversal of BST
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Create a new BST node
def newNode(item):
    temp = Node(item)
    temp.key = item
    temp.left = temp.right = None
    return temp

# Insert a new node with a given key in the BST
def insert(node, key):
    # If the tree is empty, return a new node
    if node is None:
        return newNode(key)

    # Otherwise, recur down the tree
    if key < node.key:
        node.left = insert(node.left, key)
    elif key > node.key:
        node.right = insert(node.right, key)

    # Return the node pointer
    return node

# Inorder traversal of BST
def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)

if __name__ == '__main__':
    # Let's create the following BST
    #          50
    #       /     \
    #     30      70
    #    /  \    /  \
    #  20   40  60   80
    root = None
    # Creating the BST
    root = insert(root, 50)
    insert(root, 30)
    insert(root, 20)
    insert(root, 40)
    insert(root, 70)
    insert(root, 60)
    insert(root, 80)
    # Function Call
    inorder(root)

# OUTPUT:
# 20 30 40 50 60 70 80
```

### Preorder traversal

Preorder traversal **first visits the root node**, then **traverses the left and the right subtrees**.
It is ***used to create a copy of the tree***.
Preorder traversal is also used to ***get a prefix expression(s) of an expression tree***.

**Time Complexity**: `O(N)`, where `N` is the number of nodes of the BST
**Space Complexity**: `O(1)`

```python
# Python program to implement preorder traversal
class Node:
    # Constructor to create a new node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(node, key):
    # If the tree is empty, return a new node
    if node is None:
        return Node(key)

    # Otherwise, recur down the tree
    if key < node.key:
        node.left = insert(node.left, key)
    elif key > node.key:
        node.right = insert(node.right, key)

    # Return the node pointer
    return node

def preOrder(root):
    if root:
        print(root.key, end=" ")
        preOrder(root.left)
        preOrder(root.right)

if __name__ == '__main__':
    """
        Let us create following BST
              50
           /     \
          30      70
         /  \    /  \
       20   40  60   80
   """
    root = None
    keys = [50, 30, 20, 40, 70, 60, 80]
    # Creating the BST
    for key in keys:
        root = insert(root, key)

    # Function Call
    preOrder(root)

# OUTPUT:
# 50 30 20 40 70 60 80
```

### Postorder traversal

Postorder traversal first ***traverses the left*** and the ***right subtree***, then visits the ***root node***.
It is used to ***delete the tree***. In simple words, it visits the root of every subtree last.

**Time Complexity**: `O(N)`, where `N` is the number of nodes of the BST
**Space Complexity**: `O(1)`

```python
# Python program to implement postorder traversal
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(node, key):
    # If the tree is empty, return a new node
    if node is None:
        return Node(key)

    # Otherwise, recur down the tree
    if key < node.key:
        node.left = insert(node.left, key)
    elif key > node.key:
        node.right = insert(node.right, key)

    # Return the node pointer
    return node

def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root.key, end=" ")

if __name__ == '__main__':
    # Create BST:
    #           50
    #        /     \
    #       30      70
    #      /  \    /  \
    #    20   40  60   80

    root = None
    root = insert(root, 50)
    insert(root, 30)
    insert(root, 20)
    insert(root, 40)
    insert(root, 70)
    insert(root, 60)
    insert(root, 80)
    # Function call
    postOrder(root)

# OUTPUT:
# 20 40 30 60 80 70 50
```

### Level order traversal

Level order traversal of a BST is a **Breadth First** traversal for the BST.
It visits all nodes at a particular level first before moving to the next level.

**Time Complexity**: `O(N)`, where `N` is the number of nodes of the BST
**Space Complexity**: `O(1)`

```python
# Python program to implement level order traversal
import queue

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Insert a new node with a given key in BST
def insert(node, key):
    # If the tree is empty, return a new node
    if node is None:
        return Node(key)

    # Otherwise, recur down the tree
    if key < node.key:
        node.left = insert(node.left, key)
    elif key > node.key:
        node.right = insert(node.right, key)

    # Return the node pointer
    return node

# Returns height of the BST
def height(node):
    if node is None:
        return 0
    else:
        # Compute the depth of each subtree
        lDepth = height(node.left)
        rDepth = height(node.right)

        # Use the larger one
        if lDepth > rDepth:
            return (lDepth + 1)
        else:
            return (rDepth + 1)

# Print nodes at a given level
def printGivenLevel(root, level):
    if root is None:
        return
    if level == 1:
        print(root.key, end=" ")
    elif level > 1:
        # Recursive call
        printGivenLevel(root.left, level - 1)
        printGivenLevel(root.right, level - 1)

# Function to print level order traversal of a tree, line by line
def printLevelOrder(root):
    h = height(root)
    for i in range(1, h+1):
        printGivenLevel(root, i)
        print()

if __name__ == '__main__':
    # Let us create the following BST
    #          50
    #       /     \
    #      30      70
    #     /  \    /  \
    #   20   40  60   80
    root = None

    # Create BST
    root = insert(root, 50)
    insert(root, 30)
    insert(root, 20)
    insert(root, 40)
    insert(root, 70)
    insert(root, 60)
    insert(root, 80)
    # Function Call
    printLevelOrder(root)

# Output
#  50
#  30  70
#  20  40  60  80
```
