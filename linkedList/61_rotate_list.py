# link: https://leetcode.com/problems/rotate-list/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next or k == 0:
            return head
        l, cur = 0, head
        while cur:
            l += 1
            tail = cur
            cur = cur.next

        k %= l
        if k == 0:
            return head

        cur = head
        for i in range(l - k - 1):
            cur = cur.next

        next = cur.next
        cur.next = None
        tail.next = head
        return next