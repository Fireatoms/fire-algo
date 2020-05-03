# 题目链接：https://leetcode.com/problems/valid-mountain-array/


class Solution:
    def validMountainArray(self, A):
        # 模拟向上和向下的过程，找到顶点和最低点。检查这两个点合法性来判断是否是山峰数组
        i = 0
        ln = len(A)
        # 循环终止条件要考虑清楚，模拟上升过程
        while i < ln - 1 and A[i] < A[i+1]:
            i += 1

        if i == 0 or i == ln - 1:
            return False

        # 模拟下坡过程
        while i < ln - 1 and A[i] > A[i+1]:
            i += 1

        return i == ln - 1