# link: https://leetcode-cn.com/problems/merge-k-sorted-lists/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None

        amount = len(lists)
        interval = 1

        while interval < amount:
            for i in range(0, amount - interval, 2 * interval):
                lists[i] = self.merge(lists[i], lists[i + interval])
            interval *= 2

        return lists[0]

    def merge(self, l, r):
        if not l or not r:
            return l or r

        dummy = ListNode()
        cur = dummy

        while l and r:
            if l.val <= r.val:
                cur.next = l
                l = l.next
            else:
                cur.next = r
                r = r.next
            cur = cur.next

        cur.next = l or r

        return dummy.next