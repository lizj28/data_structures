from app.linked_list import ListNode, LinkedList


def test_has_next():
    node: ListNode = ListNode("data")
    next_node: ListNode = ListNode("more data")
    node.next = next_node

    assert node.has_next() is True
    assert next_node.has_next() is False


def test_is_empty():
    list: LinkedList = LinkedList()
    list_2: LinkedList = LinkedList()
    list_node: ListNode = ListNode("data")
    list_2.head = list_node

    assert list.is_empty() is True
    assert list_2.is_empty() is False


def test_insert_first():
    list: LinkedList = LinkedList()
    list_node: ListNode = ListNode("data")
    list.head = list_node

    list_node_2: ListNode = ListNode("data 2")
    list.insert(list_node_2)

    assert list.head == list_node_2
    assert list.head.next == list_node

