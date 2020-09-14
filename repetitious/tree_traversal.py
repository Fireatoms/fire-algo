# preorder 144 94 inorder 145 postorder
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorder_iter(root):
    res, stack = [], []
    if root:
        stack.append(root)

    while stack:
        cur = stack.pop()
        res.append(cur.val)
        if cur.right:
            stack.append(cur.right)
        if cur.left:
            stack.append(cur.left)

    return res

def postorder_iter(root):
    res, stack = deque(), []
    if root:
        stack.append(root)

    while stack:
        cur = stack.pop()
        res.appendleft(cur.val)
        if cur.left:
            stack.append(cur.left)
        if cur.right:
            stack.append(cur.right)

    return list(res)

def inorder_iter(root):
    res, stack = [], []
    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        node = stack.pop()
        res.append(node.val)
        root = node.right
    return res