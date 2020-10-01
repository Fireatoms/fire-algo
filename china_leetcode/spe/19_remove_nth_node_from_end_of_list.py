# link: https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head

        fast = dummy
        slow = dummy
        slow_pre = dummy
        for i in range(n):
            fast = fast.next

        while fast:
            fast = fast.next
            slow_pre = slow
            slow = slow.next

        slow_pre.next = slow.next
        return dummy.next