# link: https://leetcode-cn.com/problems/validate-binary-search-tree/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution2:
    def __init__(self):
        self.pre = float("-inf")

    def isValidBST(self, root: TreeNode) -> bool:
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            node = stack.pop()
            if node.val <= self.pre:
                return False
            self.pre = node.val
            root = node.right
        return True


class Solution1:
    def __init__(self):
        self.node_stack = []
        self.lowers = []
        self.uppers = []

    def update(self, node, lower, upper):
        self.node_stack.append(node)
        self.lowers.append(lower)
        self.uppers.append(upper)

    def pop(self):
        return self.node_stack.pop(), self.lowers.pop(), self.uppers.pop()

    def isValidBST(self, root: TreeNode) -> bool:
        self.update(root, float("-inf"), float("inf"))
        while self.node_stack:
            node, lower, upper = self.pop()
            if not node:
                continue
            if node.val <= lower or node.val >= upper:
                return False
            self.update(node.left, lower, node.val)
            self.update(node.right, node.val, upper)
        return True

    def print_list(self, node_list):
        for i in node_list:
            print(i.val, end=" ")
        print("\n")

class Solution:
    def __init__(self):
        self.pre = float("-inf")

    def isValidBST(self, root: TreeNode) -> bool:
        if root is None:
            return True

        if not self.isValidBST(root.left):
            return False
        if root.val <= self.pre:
            return False
        self.pre = root.val
        return self.isValidBST(root.right)

    def isValidBSTRecur(self, root: TreeNode) -> bool:
        return self.is_valid_r(root, float("-inf"), float("inf"))

    def is_valid_r(self, root, min, max):
        if root is None:
            return True
        if root.val <= min or root.val >= max:
            return False
        return self.is_valid_r(root.left, min, root.val) and \
               self.is_valid_r(root.right, root.val, max)


if __name__ == "__main__":
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    sl = Solution2()
    print(sl.isValidBST(root))