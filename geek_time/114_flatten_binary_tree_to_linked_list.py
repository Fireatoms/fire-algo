# link: https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        cur = root
        while cur:
            pre = cur.left
            while pre and pre.right:
                pre = pre.right
            if pre:
                pre.right = cur.right
                cur.right = cur.left
                cur.left = None
            cur = cur.right

    def flatten_pre_iter_modify(self, root: TreeNode) -> None:
        if not root:
            return

        stack = [root]
        pre = None
        while stack:
            cur = stack.pop()
            if pre:
                pre.left = None
                pre.right = cur
            if cur.right: stack.append(cur.right)
            if cur.left: stack.append(cur.left)
            pre = cur

    def flatten_pre_iter(self, root: TreeNode) -> None:
        if not root:
            return

        preorder_list = []
        stack = [root]
        while stack:
            node = stack.pop()
            preorder_list.append(node)
            if node.right: stack.append(node.right)
            if node.left: stack.append(node.left)

        for i in range(1, len(preorder_list)):
            pre, cur = preorder_list[i-1], preorder_list[i]
            pre.left = None
            pre.right = cur

    def flatten_in(self, root: TreeNode) -> None:
        pre = None
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            cur = stack.pop()
            if pre:
                pre.right = cur
                pre.left = None
            root = cur.right
            pre = cur

    def flatten_pre_store_r(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        preorder_list = []
        self.preorder_r(root, preorder_list)
        for i in range(1, len(preorder_list)):
            pre, cur = preorder_list[i-1], preorder_list[i]
            pre.left = None
            pre.right = cur

    def preorder_r(self, root, preorder_list):
        if not root:
            return
        preorder_list.append(root)
        self.preorder_r(root.left, preorder_list)
        self.preorder_r(root.right, preorder_list)


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(6)
    sl = Solution()
    sl.flatten(root)
    print(root)
    print("done")
