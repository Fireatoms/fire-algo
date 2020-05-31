# link: https://leetcode.com/problems/two-sum-iv-input-is-a-bst/solution/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        """two sum问题，解题的核心逻辑是相同的，用hash存储已遍历结点，新遍历结点：target - value检查是不是在hash表中"""
        if root is None:
            return False

        v_set = set()
        is_find = [False]
        # 只要是遍历就行，这里选取中序遍历来实现
        self.in_order_traverse(root, v_set, k, is_find)
        return is_find[0]

    def in_order_traverse(self, root, v_set, k, is_find):
        if root is None:
            return

        self.in_order_traverse(root.left, v_set, k, is_find)
        if k - root.val in v_set:
            is_find[0] = True
            return
        v_set.add(root.val)
        self.in_order_traverse(root.right, v_set, k, is_find)

class Solution1:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        """纯递归实现，不考虑前中后序遍历或者按层遍历这些
        递归啊，递归，真的要多练，多理解，否则很难搞
        递推公式：find_base(p, k, v_set) = find_base(p.left, k, v_set) || find_base(p.right, k, v_set)
        终止条件：p:None or k - p.val in v_set
        """
        v_set = set()
        return self.find_base(root, k, v_set)

    def find_base(self, p, k, v_set):
        if p is None:
            return False
        if k - p.val in v_set:
            return True

        v_set.add(p.val)

        return self.find_base(p.left, k, v_set) or self.find_base(p.right, k, v_set)
