# link: https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-di-kda-jie-dian-lcof/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.ans = -1
        self.k = 0

    def kthLargest(self, root: TreeNode, k: int) -> int:
        self.k = k
        def kth_r(root):
            if not root: return
            kth_r(root.right)
            if self.k == 0: return
            self.k -= 1
            if self.k == 0: self.ans = root.val
            kth_r(root.left)
        kth_r(root)
        return self.ans

    def kthLargestRight(self, root: TreeNode, k: int) -> int:
        assist_stack = []
        while root or assist_stack:
            while root:
                assist_stack.append(root)
                root = root.right
            root = assist_stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.left
        return -1

    def kthLargestAll(self, root: TreeNode, k: int) -> int:
        traverse_list = []
        assist_stack = []
        while root or assist_stack:
            while root:
                assist_stack.append(root)
                root = root.left
            root = assist_stack.pop()
            traverse_list.append(root.val)
            root = root.right
        return traverse_list[-k]


# def test():
#     c = 1
#     def nest_test():
#         nonlocal c
#         c += 1
#     nest_test()
#     print(c)


if __name__ == "__main__":
    # test()
    sl = Solution()
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(6)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(7)
    print(sl.kthLargest(root, 3))