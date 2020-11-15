# binary tree
# preorder inorder postorder iteration recursion
from collections import deque


# array tree to linked list tree

class Node:
    def __init__(self, val=-1, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TreeUtils:
    def __init__(self):
        self.preorder = []
        self.postorder = []
        self.inorder = []

    def preorder_recur(self, root):
        if not root:
            return
        self.preorder.append(root.val)
        self.preorder_recur(root.left)
        self.preorder_recur(root.right)

    def preorder_iter(self, root):
        if not root:
            return

        stack = [root]
        while stack:
            node = stack.pop()
            self.preorder.append(node.val)
            if node.right: stack.append(node.right)
            if node.left: stack.append(node.left)

    def postorder_recur(self, root):
        if not root:
            return

        self.postorder_recur(root.left)
        self.postorder_recur(root.right)
        self.postorder.append(root.val)

    def postorder_iter(self, root):
        if not root:
            return

        stack = [root]
        queue = deque()
        while stack:
            node = stack.pop()
            queue.appendleft(node.val)
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)

        self.postorder = list(queue)

    def inorder_recur(self, root):
        if not root:
            return

        self.inorder_recur(root.left)
        self.inorder.append(root.val)
        self.inorder_recur(root.right)

    def inorder_iter(self, root):
        if not root:
            return

        node = root
        stack = []
        while stack or node:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()
            self.inorder.append(node.val)
            node = node.right

    def convert_tree(self, arr, idx):
        if idx >= len(arr):
            return
        node = Node(arr[idx])
        node.left = self.convert_tree(arr, 2 * idx + 1)
        node.right = self.convert_tree(arr, 2 * idx + 2)
        return node


if __name__ == "__main__":
    t = TreeUtils()
    arr = [i for i in range(1, 10)]
    # print(arr, id(arr))
    root = t.convert_tree(arr, 0)
    t.preorder_iter(root)
    print(t.preorder)

    # t.postorder_recur(root)
    t.postorder_iter(root)
    print(t.postorder)

    # t.inorder_recur(root)
    t.inorder_iter(root)
    print(t.inorder)

