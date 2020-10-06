# link: https://leetcode-cn.com/problems/liang-ge-lian-biao-de-di-yi-ge-gong-gong-jie-dian-lcof/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        headA_p, headB_p = headA, headB
        while headA_p != headB_p:
            headA_p = headA_p.next if headA_p else headB
            headB_p = headB_p.next if headB_p else headA

        return headA_p