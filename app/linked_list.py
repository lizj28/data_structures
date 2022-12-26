# Insertion

# Deletion

# Searching

# Traversal
class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return True


class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    def has_next(self):
        if self.next is not None:
            return True
        return False
