# link: https://leetcode-cn.com/problems/er-cha-sou-suo-shu-yu-shuang-xiang-lian-biao-lcof/


# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.pre = None
        self.head = None

    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        if self.pre:
            self.pre.right, root.left = root, self.pre
        else:
            self.head = root
        self.pre = root
        self.inorder(root.right)

    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return root
        self.inorder(root)
        self.head.left, self.pre.right = self.pre, self.head
        return self.head