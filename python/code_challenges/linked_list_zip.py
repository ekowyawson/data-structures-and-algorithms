class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f"{self.value} -> {self.next}"


def zip_lists(a, b):
    # Dummy node to start the zipped list
    dummy = ListNode()
    tail = dummy
    current1, current2 = a, b

    # Alternate between the two lists
    while current1 and current2:
        tail.next = current1
        current1 = current1.next
        tail = tail.next

        tail.next = current2
        current2 = current2.next
        tail = tail.next

    # Append the remaining nodes of the longer list
    tail.next = current1 if current1 else current2

    return dummy.next
