# link: https://leetcode-cn.com/problems/er-cha-shu-de-zui-jin-gong-gong-zu-xian-lcof/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.ans = None
        self.parents = {}

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.dfs_recur(root, p, q)
        return self.ans

    def dfs_recur(self, root, p, q):
        if not root:
            return False
        is_target_val = root.val == p.val or root.val == q.val
        lson = self.dfs_recur(root.left, p, q)
        rson = self.dfs_recur(root.right, p, q)
        if (lson and rson) or (is_target_val and (lson or rson)):
            self.ans = root
        return is_target_val or lson or rson

    def lowestCommonAncestorIter(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.dfs_parents(root)
        visited = set()
        while p.val in self.parents:
            visited.add(p)
            p = self.parents[p.val]
        while q.val in self.parents:
            if q in visited:
                return q
            q = self.parents[q.val]
        return root

    def dfs_parents(self, root):
        if not root:
            return
        if root.left: self.parents[root.left.val] = root
        if root.right: self.parents[root.right.val] = root
        self.dfs_parents(root.left)
        self.dfs_parents(root.right)


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    sl = Solution()
    print(sl.lowestCommonAncestorIter(root, root.left.right, root.left).val)