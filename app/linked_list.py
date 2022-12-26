# Insertion

# Deletion

# Searching

# Traversal
# class LinkedList:


class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    def has_next(self):
        if self.next is not None:
            return True
        return False
