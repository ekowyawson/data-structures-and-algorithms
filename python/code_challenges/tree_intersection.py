from data_structures.hashtable import Hashtable

def tree_intersection(tree1, tree2):
    """Finds the intersection of values between two binary trees.
    This function traverses two binary trees and returns a set of values
    that are found in both trees. It utilizes a Hashtable to efficiently
    track the values encountered in the first tree and then checks for
    their existence in the second tree.

    params:
    ------
        `tree1`: The first binary tree.
        `tree2`: The second binary tree.

    returns:
    -------
        A set of intersecting values found in both trees.
    """
    hashtable = Hashtable()
    intersecting_values = set()

    def traverse_and_store(node):
        """Traverses a binary tree in a pre-order manner and stores each
        node's value in the hashtable.

        params:
        ------
            `node`: The current node in the binary tree.
        """
        if node:
            hashtable.set(node.value, True)
            traverse_and_store(node.left)
            traverse_and_store(node.right)

    def traverse_and_check(node):
        """Traverses a binary tree in a pre-order manner and adds each node's
        value to the set of intersecting values if it exists in the hashtable.

        params:
        ------
            `node`: The current node in the binary tree.
        """
        if node:
            if hashtable.has(node.value):
                intersecting_values.add(node.value)
            traverse_and_check(node.left)
            traverse_and_check(node.right)

    # Start traversal from the root node of each BinaryTree
    traverse_and_store(tree1.root)
    traverse_and_check(tree2.root)

    return intersecting_values
