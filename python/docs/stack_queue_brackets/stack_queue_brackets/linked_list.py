# from dataclasses import dataclass

class TargetError(Exception):
    """Exception raised when a target value is not found in the linked list."""
    pass

# @dataclass
class Node:
    """A class representing a node in a linked list.

    Attributes:
        value (any): The value stored in the node.
        next (Node): A pointer to the next node in the linked list.
    """
    # value: any
    # next: 'Node' = None
    def __init__(self, value):
        self.value = value
        self.next = None

# @dataclass
class LinkedList:
    """A class representing a singly linked list.

    Attributes:
        head (Node): The first node in the linked list.

    Methods:
        insert(value): Inserts a new node with the given value at the beginning of the list.
        includes(value): Checks if a value is present in the list.
        to_string(): Returns a string representation of the list.
    """
    # head: Node = None
    def __init__(self):
        self.head = None

    def insert(self, value):
        """Inserts a new Node at the beginning of the linked list.

        Parameters:
            value (any): The value to be stored in the new node.

        Returns:
            None
        """
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def includes(self, value):
        """Checks if the linked list includes a node with the given value.

        Parameters:
            value (any): The value to search for in the list.

        Returns:
            bool: True if the value is found, False otherwise.
        """
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def to_string(self):
        """Generates a string representation of the linked list.

        Returns:
            str: A string representing the values in the linked list,
                 in the format of: "{ a } -> { b } -> { c } -> NULL".
        """
        string_representation = ""
        current = self.head
        while current:
            string_representation += f"{{ {current.value} }} -> "
            current = current.next
        string_representation += "NULL"
        return string_representation

    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def insert_before(self, value, new_value):
        if self.head is None:
            raise TargetError("List is empty, target value not found.")

        new_node = Node(new_value)
        if self.head is None or self.head.value == value:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        while current.next is not None and current.next.value != value:
            current = current.next

        if current.next is None:
            raise TargetError(f"Target value {value} not found in the list.")
        else:
            new_node.next = current.next
            current.next = new_node

    def insert_after(self, value, new_value):
        if self.head is None:
            raise TargetError("List is empty, target value not found.")

        current = self.head
        while current is not None:
            if current.value == value:
                new_node = Node(new_value)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next

        raise TargetError(f"Target value {value} not found in the list.")

    def __str__(self):
        values = []
        current = self.head
        while current:
            values.append(f"{{ {current.value} }} -> ")
            current = current.next
        return ''.join(values) + 'NULL'

# Example usage of the LinkedList class
# linked_list = LinkedList()
# linked_list.insert({'meat':'crab','veggie':'broccoli'})
# linked_list.insert(3)
# linked_list.insert(2)
# linked_list.insert(1)
# linked_list.append(10)
# linked_list.insert_before(10, 5)
# linked_list.insert_after(10, 15)
# linked_list.insert_after(15, 25)
# linked_list.insert_before(5, 3)

# print("Linked List:", linked_list.to_string())
# print("Includes 2:", linked_list.includes(2))
# print("Includes 4:", linked_list.includes(4))
