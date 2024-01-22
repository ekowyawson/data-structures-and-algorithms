from dataclasses import dataclass

@dataclass
class Node:
    """A class representing a node in a linked list.

    Attributes:
        value (any): The value stored in the node.
        next (Node): A pointer to the next node in the linked list.
    """
    value: any
    next: 'Node' = None

@dataclass
class LinkedList:
    """A class representing a singly linked list.

    Attributes:
        head (Node): The first node in the linked list.

    Methods:
        insert(value): Inserts a new node with the given value at the beginning of the list.
        includes(value): Checks if a value is present in the list.
        to_string(): Returns a string representation of the list.
    """
    head: Node = None

    def insert(self, value):
        """Inserts a new Node at the beginning of the linked list.

        Parameters:
            value (any): The value to be stored in the new node.

        Returns:
            None
        """
        new_node = Node(value, self.head)
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

# Example usage of the LinkedList class
# linked_list = LinkedList()
# linked_list.insert({'meat':'crab','veggie':'broccoli'})
# linked_list.insert(3)
# linked_list.insert(2)
# linked_list.insert(1)

# print("Linked List:", linked_list.to_string())
# print("Includes 2:", linked_list.includes(2))
# print("Includes 4:", linked_list.includes(4))
