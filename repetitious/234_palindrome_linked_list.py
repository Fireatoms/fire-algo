# link: https://leetcode.com/problems/palindrome-linked-list/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True

        # find middle node
        fast = head
        slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow

        # reverse list from the middle node
        pre = None
        cur = mid
        while cur:
            third = cur.next
            cur.next = pre
            pre = cur
            cur = third

        mid_begin = pre
        while head and mid_begin:
             if head.val != mid_begin.val:
                 return False
             head = head.next
             mid_begin = mid_begin.next

        return True