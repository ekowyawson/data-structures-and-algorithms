class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f"{self.value} -> {self.next}"


def zip_lists(a, b):
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
        current2 = next2

    return a
