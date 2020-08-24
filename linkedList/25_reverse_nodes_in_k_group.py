# link: https://leetcode.com/problems/reverse-nodes-in-k-group/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        n = 0
        cur = head
        while cur and n < k:
            cur = cur.next
            n += 1

        if k <= 1 or n < k:
            return head

        cur = head
        pre = None
        n = 0
        while n < k:
            third = cur.next
            cur.next = pre
            pre = cur
            cur = third
            n += 1

        head.next = self.reverseKGroup(cur, k)
        return pre