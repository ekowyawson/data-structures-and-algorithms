class ListNode:
    """A class representing a node in a linked list.
    Attributes:
        value (Any): The value stored in the node.
        next (ListNode, optional): A reference to the next node in the linked list. Default is None.
    Methods:
        __repr__: Provides a string representation of the node and its subsequent nodes.
    """

    def __init__(self, value=0, next=None):
        """Initialize a ListNode with a value and a reference to the next node.
        Parameters:
            value (Any): The value to store in the node.
            next (ListNode, optional): The next node in the linked list. Default is None.
        """
        self.value = value
        self.next = next

    def __repr__(self):
        """Generate a string representation of the node and its subsequent nodes.
        Returns:
            str: A string representation of the node in the format "value -> next".
        """
        return f"{self.value} -> {self.next}"


def zip_lists(a, b):
    """Zips two linked lists into one by alternating their nodes.
    This function modifies the lists in place by changing the 'next' pointers of the nodes.
    The resulting list will start with the head of 'a', followed by the head of 'b', and so on.
    If one list is shorter, the remaining nodes of the longer list will be appended at the end.

    Parameters:
        a (LinkedList): The first linked list to be zipped.
        b (LinkedList): The second linked list to be zipped.
    Returns:
        LinkedList: The head of the zipped linked list. If 'a' is non-empty, it returns 'a';
                    otherwise, it returns 'b'.
    """
    if not a.head:
        return b
    if not b.head:
        return a

    current1, current2 = a.head, b.head
    next1, next2 = None, None

    while current1 and current2:
        next1, next2 = current1.next, current2.next

        current2.next = next1
        current1.next = current2

        current1 = next1
        if not current1:
            current2.next = next2
            break

        current2 = next2

    return a
