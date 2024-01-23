from stack_queue_pseudo.stack import Node
from stack_queue_pseudo.invalid_operation_error import InvalidOperationError

class Stack:
    """
    A Stack data structure class.

    Implements a Last In, First Out (LIFO) data structure using a linked list.

    Attributes:
        top (Node): A pointer to the top node in the stack. Initially None.
    """

    def __init__(self):
        """Initialize an empty stack."""
        self.top = None

    def push(self, value):
        """
        Push a new value onto the stack.

        Creates a new Node with the given value and places it on top of the stack.

        Args:
            value: The value to be stored in the stack.
        """
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        """
        Pop the top value from the stack and return it.

        Removes the top node from the stack and returns its value.
        Raises InvalidOperationError if the stack is empty.

        Returns:
            The value stored in the node at the top of the stack.

        Raises:
            InvalidOperationError: If the stack is empty.
        """
        if self.is_empty():
            raise InvalidOperationError()
        value = self.top.value
        self.top = self.top.next
        return value

    def peek(self):
        """
        Return the top value of the stack without removing it.

        Provides the value of the top node without modifying the stack.
        Raises InvalidOperationError if the stack is empty.

        Returns:
            The value stored in the node at the top of the stack.

        Raises:
            InvalidOperationError: If the stack is empty.
        """
        if self.is_empty():
            raise InvalidOperationError()
        return self.top.value

    def is_empty(self):
        """
        Check if the stack is empty.

        Returns True if the stack has no elements, False otherwise.

        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return self.top is None
