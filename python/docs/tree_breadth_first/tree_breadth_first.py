from collections import deque

def breadth_first(tree):
    """
    Perform a breadth-first traversal of a binary tree and return a list of values
    in the order they were encountered.

    Args:
        tree (Tree): The binary tree to traverse.

    Returns:
        List: A list of values from the tree in the order they were encountered.
    """
    if not tree or not tree.root:
        return []

    queue = deque([tree.root])
    values = []

    while queue:
        current_node = queue.popleft()
        values.append(current_node.key)

        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)

    return values
