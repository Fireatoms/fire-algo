# link: https://leetcode.com/problems/binary-search-tree-iterator/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self._sorted_arr = []
        self._index = 0
        self._inorder(root)

    def _inorder(self, root):
        if not root:
            return
        self._inorder(root.left)
        self._sorted_arr.append(root.val)
        self._inorder(root.right)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        val = self._sorted_arr[self._index]
        self._index += 1
        return val


    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self._index <= len(self._sorted_arr) - 1

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIteratorIter:

    def __init__(self, root: TreeNode):
        self._stack = []
        self._leftmost_inorder(root)

    def _leftmost_inorder(self, node):
        while node:
            self._stack.append(node)
            node = node.left

    def next(self) -> int:
        """
        @return the next smallest number
        """
        node = self._stack.pop()
        if node.right:
            self._leftmost_inorder(node.right)
        return node.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self._stack) > 0