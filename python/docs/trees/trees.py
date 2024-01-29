class Node:
    """A Node in a binary tree containing a value and references to its left and right children.
    """
    def __init__(self, value):
        """Initializes a Node with a specified value.

        `Parameters`:
            `value`: The value to be stored in the node.
        """
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    """Binary tree class for creating and traversing binary trees."""
    def __init__(self):
        """Initializes an empty binary tree."""
        self.root = None

    def pre_order(self):
        """Performs a pre-order traversal of the binary tree.

        Returns:
            A list of values in the tree following the pre-order sequence.
        """
        return self._traverse_pre_order(self.root, [])

    def _traverse_pre_order(self, node, values):
        """Helper method for pre_order to recursively traverse the tree.

        `Parameters`:
            `node`: The current node being traversed.
            `values`: The list of accumulated values.

        `Returns`:
            The list of values accumulated so far.
        """
        if node:
            values.append(node.value)
            self._traverse_pre_order(node.left, values)
            self._traverse_pre_order(node.right, values)
        return values

    def in_order(self):
        """
        Performs an in-order traversal of the binary tree.

        `Returns`:
            A list of values in the tree following the in-order sequence.
        """
        return self._traverse_in_order(self.root, [])

    def _traverse_in_order(self, node, values):
        """Helper method for in_order to recursively traverse the tree.

        `Parameters`:
            `node`: The current node being traversed.
            `values`: The list of accumulated values.

        `Returns`:
            The list of values accumulated so far.
        """
        if node:
            self._traverse_in_order(node.left, values)
            values.append(node.value)
            self._traverse_in_order(node.right, values)
        return values

    def post_order(self):
        """Performs a post-order traversal of the binary tree.

        `Returns`:
            A list of values in the tree following the post-order sequence.
        """
        return self._traverse_post_order(self.root, [])

    def _traverse_post_order(self, node, values):
        """Helper method for post_order to recursively traverse the tree.

        `Parameters`:
            `node`: The current node being traversed.
            `values`: The list of accumulated values.

        `Returns`:
            The list of values accumulated so far.
        """
        if node:
            self._traverse_post_order(node.left, values)
            self._traverse_post_order(node.right, values)
            values.append(node.value)
        return values


class BinarySearchTree(BinaryTree):
    """Binary Search Tree class, a subclass of BinaryTree, with additional methods for insertion and search."""
    def add(self, value):
        """Adds a new node with the specified value to the binary search tree.

        `Parameters`:
            `value`: The value to be added to the tree.
        """
        if not self.root:
            self.root = Node(value)
        else:
            self._add(value, self.root)

    def _add(self, value, node):
        """Helper method for add to recursively find the correct position for the new value.

        `Parameters`:
            `value`: The value to be added.
            `node`: The current node being compared.
        """
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._add(value, node.left)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._add(value, node.right)

    def contains(self, value):
        """Checks whether the binary search tree contains a given value.

        `Parameters`:
            `value`: The value to search for in the tree.

        `Returns`:
            Boolean indicating whether the value is present in the tree.
        """
        return self._contains(value, self.root)

    def _contains(self, value, node):
        """Helper method for contains to recursively search for the value.

        `Parameters`:
            `value`: The value to search for.
            `node`: The current node being checked.

        `Returns`:
            Boolean indicating whether the value is present in the subtree rooted at the current node.
        """
        if not node:
            return False
        if value == node.value:
            return True
        elif value < node.value:
            return self._contains(value, node.left)
        else:
            return self._contains(value, node.right)
