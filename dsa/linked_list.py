class LinkedList:
    def __init__(self, values=None):
        self.head = None
        if values:
            for value in reversed(values):
                self.insert(value)

    def insert(self, value):
        self.head = Node(value, self.head)

    def to_list(self):
        values = []
        current = self.head
        while current:
            values.append(current.value)
            current = current.next

        return values


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
