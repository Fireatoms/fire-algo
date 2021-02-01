# link: https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof/
from typing import List


class Solution:
    def verify_r(self, postorder, i, j):
        if i >= j:
            return True
        p = i
        while postorder[p] < postorder[j]:
            p += 1
        m = p
        while postorder[p] > postorder[j]:
            p += 1
        return p == j and self.verify_r(postorder, i, m - 1) and self.verify_r(postorder, m, j - 1)

    def verifyPostorder(self, postorder: List[int]) -> bool:
        return self.verify_r(postorder, 0, len(postorder) - 1)