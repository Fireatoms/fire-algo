# link: https://leetcode-cn.com/problems/liang-ge-lian-biao-de-di-yi-ge-gong-gong-jie-dian-lcof/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        headA_pointer, headB_pointer = headA, headB

        while headA_pointer != headB_pointer:
            headA_pointer = headA_pointer.next if headA_pointer else headB
            headB_pointer = headB_pointer.next if headB_pointer else headA

        return headA_pointer