class TreeNode:
    def __init__(self, data: int):
        self.right_child = None
        self.left_child = None
        self.data = data

# Removal
# Search
# Height of tree
class BinaryTree:
    def __init__(self):
        self.root = None

    def is_empty(self):
        if self.root is None:
            return True
        return False

    def insert(self, root_node: TreeNode, node: TreeNode):
        if root_node is None:
            root_node = node
            return root_node
        if root_node.data <= node.data:
            root_node.right_child = self.insert(root_node.right_child, node)
        elif root_node.data > node.data:
            root_node.left_child = self.insert(root_node.left_child, node)
        return root_node

    def find(self, root_node: TreeNode, val):
        if root_node is None:
            return None
        if val == root_node.data:
            return root_node
        if val > root_node.data:
            return self.find(root_node.right_child, val)
        elif val < root_node.data:
            return self.find(root_node.left_child, val)
