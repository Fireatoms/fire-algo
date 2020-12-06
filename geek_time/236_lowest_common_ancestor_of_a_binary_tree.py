# link: https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution1:
    def __init__(self):
        self.parents = {}

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # self.get_parents_recur(root)
        self.get_parents_iter_dfs(root)
        # self.get_parents_iter_bfs(root)
        self.parents[root] = None
        visited = set()
        while p:
            visited.add(p)
            p = self.parents[p]
        while q not in visited:
            q = self.parents[q]
        return q

    def get_parents_iter_bfs(self, root):
        queue = deque([root])
        while queue:
            node = queue.popleft()
            print(node.val)
            if node.left:
                self.parents[node.left] = node
                queue.append(node.left)
            if node.right:
                self.parents[node.right] = node
                queue.append(node.right)

    def get_parents_iter_dfs(self, root):
        stack = [root]
        while stack:
            node = stack.pop()
            if node.right:
                self.parents[node.right] = node
                stack.append(node.right)
            if node.left:
                self.parents[node.left] = node
                stack.append(node.left)

    def get_parents_recur(self, root):
        if not root:
            return
        if root.left:
            self.parents[root.left] = root
            self.get_parents_recur(root.left)
        if root.right:
            self.parents[root.right] = root
            self.get_parents_recur(root.right)


class Solution:
    def __init__(self):
        self.path = []
        self.path_res = []
        self.ans = None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.dfs_recur(root, p, q)
        return self.ans

    def dfs_recur(self, root, p, q):
        if not root:
            return False
        print("递" + str(root.val), end=" ")
        is_current = root == p or root == q
        lson = self.dfs_recur(root.left, p, q)
        rson = self.dfs_recur(root.right, p, q)
        if (lson and rson) or ((is_current) and (lson or rson)):
            self.ans = root
        print("归" + str(root.val), end=" ")
        return lson or rson or is_current

    def lowestCommonAncestorPath(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_path = self.get_path(root, p)
        q_path = self.get_path(root, q)

        i = 0
        ans = None
        while i < len(p_path) and i < len(q_path) and p_path[i] == q_path[i]:
            ans = p_path[i]
            i += 1
        return ans

    def get_path(self, root, target):
        self.path.clear()
        self.path_res.clear()
        self.dfs(root, target)
        return self.path_res[0]

    def dfs(self, root, target):
        if not root:
            return
        self.path.append(root)
        if root == target:
            self.path_res.append(list(self.path))
            return
        self.dfs(root.left, target)
        self.dfs(root.right, target)
        self.path.pop()

    def print_path(self, path):
        res = [p.val for p in path]
        print("=>".join(map(str, res)))


class TestScope:
    def __init__(self):
        self.path = []

    def get_path_t(self, root, target):
        self.found(root, target)

    def found(self, root, target):
        if not root:
            return False
        if root == target:
            return True
        if self.found(root.left, target) or self.found(root.right, target):
            self.path.append(root)
            return True
        return False

    def print_path(self, path):
        route = []
        for p in path:
            route.append(p.val)
        print("=>".join(map(str, route)))


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)

    # p = root.left
    # q = root.left.right.right

    sl = Solution1()
    p = root.left
    q = root.right
    print(sl.lowestCommonAncestor(root, p, q).val)
    print(sl.parents)

    # sl = Solution()
    # sl.print_path(sl.allCommonAncestors(root, p, q))
    # sl.print_path(sl.get_path(root, q))
    # print(sl.lowestCommonAncestor(root, p, q).val)
    # sl.lowestCommonAncestor(root, p, q)