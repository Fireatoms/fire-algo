# link: https://leetcode.com/problems/reverse-linked-list/description/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # iteration
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        cur = head

        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp

        return pre


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class SolutionRecur:
    # recursive
    def reverseList(self, head: ListNode) -> ListNode:
        return self.reverse_r(head, None)

    def reverse_r(self, cur, pre):
        if cur is None:
            return pre

        tmp = cur.next
        cur.next = pre
        # transfer data between layers
        return self.reverse_r(tmp, cur)


class SolutionRecurGlobalVariable:
    # recursive
    res_head = ListNode()
    def reverseList(self, head: ListNode) -> ListNode:
        self.reverse_r(head, None)
        return self.res_head

    def reverse_r(self, cur, pre):
        if cur is None:
            self.res_head = pre
            return

        tmp = cur.next
        cur.next = pre
        # transfer data between layers
        self.reverse_r(tmp, cur)


class SolutionRecurRefer:
    # recursive
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p


class SolutionRecurReferVariable:
    res_head = ListNode()
    # recursive
    def reverseList(self, head: ListNode) -> ListNode:
        self.reverse_r(head)
        return self.res_head

    def reverse_r(self, head):
        if head is None or head.next is None:
            self.res_head = head
            return

        self.reverseList(head.next)
        head.next.next = head
        head.next = None