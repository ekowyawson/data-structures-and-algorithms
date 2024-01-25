class InvalidOperationError(Exception):
    """Custom exception for invalid operations on data structures.

    This exception is raised when an operation is performed on a data structure that is not allowed,
    such as attempting to peek or pop from an empty stack or queue.
    """

    def __init__(self, message="Method not allowed on empty collection"):
        self.message = message
        super().__init__(self.message)
