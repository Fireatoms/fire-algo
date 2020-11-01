# link: https://leetcode-cn.com/problems/linked-list-cycle-ii/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        encounter = self.has_cycle(head)
        if not encounter:
            return None

        pre = head
        while pre and encounter:
            if pre == encounter:
                return pre
            pre = pre.next
            encounter = encounter.next

    def has_cycle(self, head):
        slow, fast = head, head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return slow

        return None