# link: https://leetcode-cn.com/problems/reverse-linked-list/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def __init__(self):
        self.new_start = None

    def reverseList(self, head: ListNode) -> ListNode:
        self.reverseListRecur(head)
        return self.new_start

    def reverseListRecur(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            self.new_start = head
            return

        self.reverseListRecur(head.next)
        head.next.next = head
        head.next = None

    def reverseListIter(self, head: ListNode) -> ListNode:
        pre, cur = None, head
        while cur is not None:
            # I do not like this, too pythonic
            # cur.next, pre, cur = pre, cur, cur.next
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp

        return pre