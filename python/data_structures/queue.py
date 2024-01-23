from data_structures.linked_list import Node
from data_structures.invalid_operation_error import InvalidOperationError

class Queue:
    """
    A Queue data structure class.

    Implements a First In, First Out (FIFO) data structure using a linked list.

    Attributes:
        front (Node): A pointer to the front node in the queue. Initially None.
        rear (Node): A pointer to the rear node in the queue. Initially None.
    """

    def __init__(self):
        """Initialize an empty queue."""
        self.front = None
        self.rear = None

    def enqueue(self, value):
        """
        Enqueue a new value into the queue.

        Adds a new Node with the given value to the end (rear) of the queue.

        Args:
            value: The value to be stored in the queue.
        """
        node = Node(value)
        if self.is_empty():
            self.front = self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        """
        Dequeue the front value from the queue and return it.

        Removes the front node from the queue and returns its value.
        Raises InvalidOperationError if the queue is empty.

        Returns:
            The value stored in the node at the front of the queue.

        Raises:
            InvalidOperationError: If the queue is empty.
        """
        if self.is_empty():
            raise InvalidOperationError()
        value = self.front.value
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return value

    def peek(self):
        """
        Return the front value of the queue without removing it.

        Provides the value of the front node without modifying the queue.
        Raises InvalidOperationError if the queue is empty.

        Returns:
            The value stored in the node at the front of the queue.

        Raises:
            InvalidOperationError: If the queue is empty.
        """
        if self.is_empty():
            raise InvalidOperationError()
        return self.front.value

    def is_empty(self):
        """
        Check if the queue is empty.

        Returns True if the queue has no elements, False otherwise.

        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return self.front is None
