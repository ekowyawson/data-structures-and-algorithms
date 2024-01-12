from dataclasses import dataclass

@dataclass
class Node:
    value: any
    next: 'Node' = None

@dataclass
class LinkedList:
    head: Node = None

    def insert(self, value):
        new_node = Node(value, self.head)
        self.head = new_node

    def includes(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def to_string(self):
        string_representation = ""
        current = self.head
        while current:
            string_representation += f"{{ {current.value} }} -> "
            current = current.next
        string_representation += "NULL"
        return string_representation

# Example usage of the LinkedList class
linked_list = LinkedList()
linked_list.insert(3)
linked_list.insert(2)
linked_list.insert(1)

print("Linked List:", linked_list.to_string())
print("Includes 2:", linked_list.includes(2))
print("Includes 4:", linked_list.includes(4))