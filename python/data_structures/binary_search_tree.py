from data_structures.binary_tree import BinaryTree, Node


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
