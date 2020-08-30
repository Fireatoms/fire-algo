# link: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""

        que = deque([root])
        res = []
        while que:
            node = que.popleft()
            if node:
                que.append(node.left)
                que.append(node.right)
                res.append(str(node.val))
            else:
                res.append('#')
        return ','.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        nodes = data.split(',')
        root = TreeNode(int(nodes[0]))
        que = deque([root])
        index = 1
        while que:
            node = que.popleft()
            if nodes[index] != '#':
                node.left = TreeNode(int(nodes[index]))
                que.append(node.left)
            index += 1

            if nodes[index] != '#':
                node.right = TreeNode(int(nodes[index]))
                que.append(node.right)
            index += 1
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))