import unittest

from app.linked_list import ListNode, LinkedList


class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.list: LinkedList = LinkedList()
        self.list_node: ListNode = ListNode("data")

    def test_has_next(self):
        next_node: ListNode = ListNode("more data")
        self.list_node.next = next_node

        assert self.list_node.has_next() is True
        assert next_node.has_next() is False

    def test_is_empty(self):
        list_2: LinkedList = LinkedList()
        list_2.head = self.list_node

        assert self.list.is_empty() is True
        assert list_2.is_empty() is False

    def test_insert_first(self):
        self.list.head = self.list_node

        list_node_2: ListNode = ListNode("data 2")
        self.list.insert_first(list_node_2)

        assert self.list.head == list_node_2
        assert self.list.head.next == self.list_node

    def test_insert_last(self):
        self.list.head = self.list_node

        list_node_2: ListNode = ListNode("data 2")
        self.list.insert_last(list_node_2)

        assert self.list.head == self.list_node
        assert self.list.head.next == list_node_2

    def test_insert_at(self):
        self.list.head = self.list_node
        list_node_2: ListNode = ListNode("data 2")
        self.list.head.next = list_node_2

        list_node_3: ListNode = ListNode("data 3")
        self.list.insert_at(list_node_3, 1)

        assert self.list.head == self.list_node
        assert self.list.head.next == list_node_3
        assert self.list.head.next.next == list_node_2

