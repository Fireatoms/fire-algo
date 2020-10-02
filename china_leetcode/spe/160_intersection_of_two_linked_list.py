# link: https://leetcode-cn.com/problems/intersection-of-two-linked-lists/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        headA_pointer = headA
        headB_pointer = headB

        while headA_pointer != headB_pointer:
            headA_pointer = headA_pointer.next if headA_pointer else headB
            headB_pointer = headB_pointer.next if headB_pointer else headA

        return headA_pointer