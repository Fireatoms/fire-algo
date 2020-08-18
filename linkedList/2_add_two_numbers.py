# link: https://leetcode.com/problems/add-two-numbers/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_list = []
        l2_list = []

        while l1:
            l1_list.append(l1.val)
            l1 = l1.next

        while l2:
            l2_list.append(l2.val)
            l2 = l2.next

        num1 = 0
        num2 = 0

        for i, v in enumerate(l1_list):
            num1 += (10 ** i) * v

        for i, v in enumerate(l2_list):
            num2 += (10 ** i) * v

        res = num1 + num2

        dummy = ListNode(0)
        cur = dummy
        if res == 0:
            dummy.next = ListNode(0)
        while res:
            cur.next = ListNode(res % 10)
            res = res // 10
            cur = cur.next

        return dummy.next