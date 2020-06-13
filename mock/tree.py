# tree
from collections import deque


class Node:
    """tree node"""
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def pre_traverse(root):
    if root is None:
        return

    print(root.val)
    pre_traverse(root.left)
    pre_traverse(root.right)


def in_order(root):
    if root is None:
        return

    in_order(root.left)
    print(root.val)
    in_order(root.right)


def post_traverse(root):
    if root is None:
        return

    post_traverse(root.left)
    post_traverse(root.right)
    print(root.val)


def layer_traverse(root):
    dq = deque([root])

    while dq:
        node = dq.popleft()
        print(node.val)
        if node.left is not None:
            dq.append(node.left)
        if node.right is not None:
            dq.append(node.right)


def pre_order_iteration(root):
    """stack"""
    tree_stack = []
    tree_order = []
    tree_stack.append(root)
    while tree_stack:
        node = tree_stack.pop()
        tree_order.append(node.val)
        if node.right:
            tree_stack.append(node.right)
        if node.left:
            tree_stack.append(node.left)

    return tree_order


def in_order_itreation(root):
    """stack"""
    tree_stack = []
    tree_order = []
    while tree_stack or root:
        # push root and its all left nodes
        while root:
            tree_stack.append(root)
            root = root.left

        node = tree_stack.pop()
        tree_order.append(node.val)

        root = node.right

    return tree_order


def post_order_iteration(root):
    """stack for iteration
    queue store result
    """
    tree_stack = []
    tree_order = deque()
    tree_stack.append(root)

    while tree_stack:
        node = tree_stack.pop()
        tree_order.appendleft(node.val)
        if node.left:
            tree_stack.append(node.left)
        if node.right:
            tree_stack.append(node.right)

    return list(tree_order)


def construct_tree():
    root = Node(0)
    root.left = Node(1)
    root.right = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(4)
    root.left.left.left = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    return root


if __name__ == "__main__":
    root = construct_tree()
    print('layer: ')
    layer_traverse(root)
    print("pre_recursive: ")
    pre_traverse(root)
    print("in_recursive: ")
    in_order(root)
    print("post_recursive: ")
    post_traverse(root)
    print("pre_iteration: ")
    print(pre_order_iteration(root))
    print("in_iteration: ")
    print(in_order_itreation(root))
    print("post_iteration: ")
    print(post_order_iteration(root))


