# link: https://leetcode-cn.com/problems/reverse-nodes-in-k-group/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy

        while head:
            tail = pre
            for i in range(k):
                tail = tail.next
                if not tail:
                    return dummy.next

            reverse_next = tail.next
            tail.next = None
            head, tail = self.reverse_list(head, tail)
            pre.next = head
            tail.next = reverse_next
            pre = tail
            head = tail.next

        return dummy.next

    def reverse_list(self, head, tail):
        pre = tail.next
        cur = head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp

        return tail, head