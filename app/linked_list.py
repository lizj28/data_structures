class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    def has_next(self):
        if self.next is not None:
            return True
        return False


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
        self.insert_at(node, 0)

    def insert_last(self, node: ListNode):
        temp_node: ListNode = self.head
        while temp_node.next is not None:
            temp_node = temp_node.next
        temp_node.next = node

    def insert_at(self, node: ListNode, index: int):
        count: int = 0
        temp_node: ListNode = self.head
        if index == 0:
            node.next = self.head
            self.head = node

        while temp_node.next is not None:
            if count == index - 1:
                node.next = temp_node.next
                temp_node.next = node
                return
            temp_node = temp_node.next
            count += 1
        temp_node.next = node

    def remove_at(self, index: int):
        count: int = 0
        temp_node: ListNode = self.head
        if index == 0 and not self.is_empty():
            self.head = self.head.next

        while temp_node.next is not None:
            if count == index - 1:
                temp_node.next = temp_node.next.next
                return
            temp_node = temp_node.next
            count += 1

    def remove_first(self):
        self.remove_at(0)
