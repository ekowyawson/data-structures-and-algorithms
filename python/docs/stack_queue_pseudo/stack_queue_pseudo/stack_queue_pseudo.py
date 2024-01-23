class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

class PseudoQueue:
    """
    A class representing a queue implemented using two stacks. This implementation
    utilizes the LIFO (Last In, First Out) behavior of stacks to emulate the FIFO
    (First In, First Out) behavior of a queue.

    Attributes:
        stack1 (Stack): A stack used to enqueue elements.
        stack2 (Stack): A stack used to reverse the order of elements for dequeuing.
    """

    def __init__(self):
        """
        Initializes a new instance of PseudoQueue. This instance contains two stacks,
        stack1 and stack2, which are used to implement queue operations.
        """
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, value):
        """
        Adds a new value to the end of the queue.

        Args:
            value: The value to be added to the queue.
        """
        self.stack1.push(value)

    def dequeue(self):
        """
        Removes and returns the value at the front of the queue. If the queue is empty,
        returns None. This method utilizes two stacks to reverse the order of elements
        and achieve the FIFO behavior of a queue.

        Returns:
            The value at the front of the queue or None if the queue is empty.
        """
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        return self.stack2.pop()
