class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    def has_next(self):
        if self.next is not None:
            return True
        return False


# Insertion

# Deletion

# Searching

# Traversal
class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        if self.head is not None:
            return False
        return True

    def insert_first(self, node: ListNode):
        node.next = self.head
        self.head = node

    def insert_last(self, node: ListNode):
        temp_node: ListNode = self.head
        while temp_node.next is not None:
            temp_node = temp_node.next
        temp_node.next = node
