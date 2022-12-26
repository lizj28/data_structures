from app.linked_list import ListNode


def test_has_next():
    node: ListNode = ListNode("data")
    assert node.has_next() is False
