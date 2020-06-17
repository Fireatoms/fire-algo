# tree traverse
from collections import deque

class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


def construct_tree():
    root = TreeNode(0)
    root.left = TreeNode(1)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.left.left.left = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    return root


def pre_traversal_recursive(root):
    if root is None:
        return

    print(root.val, end=' ')
    pre_traversal_recursive(root.left)
    pre_traversal_recursive(root.right)


def pre_traversal_iteration(root):
    tree_stack = []
    tree_order = []
    tree_stack.append(root)

    while tree_stack:
        node = tree_stack.pop()
        tree_order.append(node.val)
        if node.right is not None:
            tree_stack.append(node.right)
        if node.left is not None:
            tree_stack.append(node.left)

    return tree_order


def post_traversal_recursive(root):
    if root is None:
        return

    post_traversal_recursive(root.left)
    post_traversal_recursive(root.right)
    print(root.val, end=' ')


def post_traversal_iteration(root):
    tree_stack = []
    tree_order = deque()
    tree_stack.append(root)

    while tree_stack:
        node = tree_stack.pop()
        tree_order.appendleft(node.val)
        if node.left is not None:
            tree_stack.append(node.left)
        if node.right is not None:
            tree_stack.append(node.right)

    return list(tree_order)


def in_traversal_recursive(root):
    if root is None:
        return

    in_traversal_recursive(root.left)
    print(root.val, end=' ')
    in_traversal_recursive(root.right)


def in_traversal_iteration(root):
    tree_stack = []
    tree_order = []

    while tree_stack or root:
        while root is not None:
            tree_stack.append(root)
            root = root.left

        node = tree_stack.pop()
        tree_order.append(node.val)
        root = node.right

    return tree_order


if __name__ == "__main__":
    root = construct_tree()
    print(in_traversal_iteration(root))
    # print(in_traversal_iteration(root))
    # in_traversal_recursive(root)
    # print(post_traversal_iteration(root))
    # post_traversal_recursive(root)
    # print(pre_traversal_iteration(root))
    # pre_traversal_recursive(root)