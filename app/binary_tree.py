class TreeNode:
    def __init__(self, data: int):
        self.right_child = None
        self.left_child = None
        self.data = data

# Removal
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

    def remove(self, root_node: TreeNode, val):
        if root_node is None:
            return root_node
        if root_node.data < val:
            root_node.right_child = self.remove(root_node.right_child, val)
        elif root_node.data > val:
            root_node.left_child = self.remove(root_node.left_child, val)

        if root_node.left_child is None:
            temp_node = root_node.right_child
            root_node = None
            return temp_node
        elif root_node.right_child is None:
            temp_node = root_node.left_child
            root_node = None
            return temp_node

        # this may be the hardest part for my brain - you have two children so go down the left side of the
        # subtree of the right child
        temp = root_node
        while temp.left_child is not None:
            temp = temp.left_child

        root_node.data = temp.data
        root_node.right_child = self.remove(root_node.right_child, temp.data)

        return root_node

    def height(self, root_node: TreeNode, cur_height: int = 0):
        if root_node is None:
            return cur_height
        left_height: int = self.height(root_node.left_child)
        right_height: int = self.height(root_node.right_child)

        return max(left_height, right_height) + 1
