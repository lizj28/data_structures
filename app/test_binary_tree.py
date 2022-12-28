import unittest

from app.binary_tree import BinaryTree, TreeNode


class TestBinaryTree(unittest.TestCase):
    def setUp(self):
        self.tree: BinaryTree = BinaryTree()
        self.tree_node: TreeNode = TreeNode(5)

    def test_is_empty(self):
        assert self.tree.is_empty() is True

        self.tree.root = self.tree_node
        assert self.tree.is_empty() is False

    def test_insert(self):
        self.tree.root = self.tree_node
        right_node: TreeNode = TreeNode(6)
        left_node: TreeNode = TreeNode(4)
        self.tree.insert(self.tree.root, right_node)
        self.tree.insert(self.tree.root, left_node)

        assert self.tree.root.right_child.data == 6
        assert self.tree.root.left_child.data == 4

    def test_remove(self):
        # TODO
        assert True is False

    def test_find(self):
        self.tree.root = self.tree_node
        right_node: TreeNode = TreeNode(6)
        left_node: TreeNode = TreeNode(4)
        right_right_node: TreeNode = TreeNode(8)
        self.tree.insert(self.tree.root, right_node)
        self.tree.insert(self.tree.root, left_node)
        self.tree.insert(self.tree.root, right_right_node)

        node_found: TreeNode = self.tree.find(self.tree.root, 8)
        node_not_found: TreeNode = self.tree.find(self.tree.root, 10)

        assert node_found == right_right_node
        assert node_not_found is None

    def test_height(self):
        self.tree.root = self.tree_node
        right_node: TreeNode = TreeNode(6)
        left_node: TreeNode = TreeNode(4)
        right_right_node: TreeNode = TreeNode(8)
        self.tree.insert(self.tree.root, right_node)
        self.tree.insert(self.tree.root, left_node)
        self.tree.insert(self.tree.root, right_right_node)

        assert self.tree.height(self.tree.root, 0) == 3
