from data_structures.kary_tree import KaryTree, Node

def fizz_buzz_tree(kary_tree):
    # Helper function to apply FizzBuzz to each node
    def fizz_buzz_node(node):
        # Base case: If the node is None, return None
        if node is None:
            return None

        # Apply FizzBuzz logic to the node's value
        new_value = ''
        if node.value % 3 == 0:
            new_value += 'Fizz'
        if node.value % 5 == 0:
            new_value += 'Buzz'
        if new_value == '':
            new_value = str(node.value)

        # Create a new node with the modified value
        new_node = Node(new_value)

        # Recursively apply this function to all children
        for child in node.children:
            new_node.children.append(fizz_buzz_node(child))

        return new_node

    # Apply the helper function to the root of the k-ary tree
    return KaryTree(fizz_buzz_node(kary_tree.root))
