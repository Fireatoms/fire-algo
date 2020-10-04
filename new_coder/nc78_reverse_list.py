# link: https://www.nowcoder.com/practice/75e878df47f24fdc9dc3e400ec6058ca?tpId=190&&tqId=35203&rp=1&ru=/ta/job-code-high-rd&qru=/ta/job-code-high-rd/question-ranking

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if not pHead:
            return None

        pre = None
        cur = pHead
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre