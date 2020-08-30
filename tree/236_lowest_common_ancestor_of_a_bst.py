# link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = None
        self.lowest_r(root, p, q)
        return self.ans

    def lowest_r(self, current_node, p, q):
        if not current_node:
            return False
        print(current_node.val)

        left = self.lowest_r(current_node.left, p, q)
        right = self.lowest_r(current_node.right, p, q)
        mid = current_node == p or current_node == q

        if left + right + mid >= 2:
            self.ans = current_node

        return left or right or mid


class Solution2:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = [root]
        parent_dict = {root: None}

        while p not in parent_dict or q not in parent_dict:
            node = stack.pop()
            if node.left:
                parent_dict[node.left] = node
                stack.append(node.left)
            if node.right:
                parent_dict[node.right] = node
                stack.append(node.right)

        ancestor = set()
        while p:
            # p is its own ancestor according to the question requirements
            ancestor.add(p)
            p = parent_dict[p]

        while q not in ancestor:
            q = parent_dict[q]

        return q


class Solution:

    def __init__(self):
        # Variable to store LCA node.
        self.ans = None

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def recurse_tree(current_node):

            # If reached the end of a branch, return False.
            if not current_node:
                return False

            # Left Recursion
            left = recurse_tree(current_node.left)

            # Right Recursion
            right = recurse_tree(current_node.right)
            print(current_node.val)

            # If the current node is one of p or q
            mid = current_node == p or current_node == q

            # If any two of the three flags left, right or mid become True.
            if mid + left + right >= 2:
                self.ans = current_node

            # Return True if either of the three bool values is True.
            return mid or left or right

        # Traverse the tree
        recurse_tree(root)
        return self.ans


if __name__ == "__main__":
    root = TreeNode(2)
    root.left = TreeNode(4)
    root.right = TreeNode(5)
    root.right.right = TreeNode(9)
    p = TreeNode(6)
    q = TreeNode(7)
    root.left.left = p
    root.left.right = q
    sl = Solution()
    r = sl.lowestCommonAncestor(root, p, q)