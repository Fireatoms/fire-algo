# link: https://leetcode.com/problems/sort-list/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None

        l = self.sortList(head)
        r = self.sortList(mid)
        return self.merge(l, r)

    def merge(self, l, r):
        if not l or not r:
            return l or r

        if l.val > r.val:
            l, r = r, l

        head = l
        cur = l
        l = l.next
        while l and r:
            if l.val <= r.val:
                cur.next = l
                l = l.next
            else:
                cur.next = r
                r = r.next
            cur = cur.next

        cur.next = l or r

        return head
