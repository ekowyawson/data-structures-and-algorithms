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
