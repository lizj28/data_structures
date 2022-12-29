import unittest

from app.bst.binary_tree import BinaryTree, TreeNode


class TestBinaryTree(unittest.TestCase):
    def setUp(self):
        self.tree: BinaryTree = BinaryTree()
        self.tree_node: TreeNode = TreeNode(5)

    def build_multi_level_tree(self):
        self.tree.root = self.tree_node
        self.right_node: TreeNode = TreeNode(6)
        self.left_node: TreeNode = TreeNode(4)
        self.right_right_node: TreeNode = TreeNode(8)
        self.tree.insert(self.tree.root, self.right_node)
        self.tree.insert(self.tree.root, self.left_node)
        self.tree.insert(self.tree.root, self.right_right_node)

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

    def test_find(self):
        self.build_multi_level_tree()

        node_found: TreeNode = self.tree.find(self.tree.root, 8)
        node_not_found: TreeNode = self.tree.find(self.tree.root, 10)

        assert node_found == self.right_right_node
        assert node_not_found is None

    def test_height(self):
        self.build_multi_level_tree()

        assert self.tree.height(self.tree.root, 0) == 3

    def test_remove(self):
        self.build_multi_level_tree()
        self.tree.remove(self.tree.root, 6)

        assert self.tree.height(self.tree.root, 0) == 2
        assert self.tree.find(self.tree.root, 6) is None
