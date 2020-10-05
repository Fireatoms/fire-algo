# link: https://leetcode-cn.com/problems/add-two-numbers/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        cur = dummy
        carry = 0

        while l1 or l2:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            list_sum = l1_val + l2_val + carry
            carry = list_sum // 10
            cur.next = ListNode(list_sum % 10)
            cur = cur.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        if carry:
            cur.next = ListNode(carry)

        return dummy.next