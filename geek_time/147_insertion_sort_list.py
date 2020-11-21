# link: https://leetcode-cn.com/problems/insertion-sort-list/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return head

        dummy = ListNode(0)
        dummy.next = head
        last_sorted = head
        cur = last_sorted.next

        while cur:
            if last_sorted.val <= cur.val:
                last_sorted = cur
            else:
                pre = dummy
                while pre.next.val < cur.val:
                    pre = pre.next
                last_sorted.next = cur.next
                cur.next = pre.next
                pre.next = cur
            cur = last_sorted.next

        return dummy.next