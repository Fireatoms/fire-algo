# link: https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        fast = dummy
        slow = dummy

        for i in range(n):
            fast = fast.next

        slow_pre = slow
        while fast:
            fast = fast.next
            slow_pre = slow
            slow = slow.next

        slow_pre.next = slow.next
        return dummy.next