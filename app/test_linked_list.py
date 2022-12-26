from app.linked_list import ListNode


def test_has_next():
    node: ListNode = ListNode("data")
    next_node: ListNode = ListNode("more data")
    node.next = next_node

    assert node.has_next() is True
    assert next_node.has_next() is False

