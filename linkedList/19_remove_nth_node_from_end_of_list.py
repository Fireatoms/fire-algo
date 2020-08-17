# link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Sentinel is not to introduced to simplify calculation
# class Solution:
#     def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
#         forward = head
#         back = head
#         while n:
#             forward = forward.next
#             n -= 1
#
#         while forward and forward.next:
#             forward = forward.next
#             back = back.next
#
#         if not back.next:
#             return None
#
#         back.next = back.next.next
#         return head


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        forward = dummy
        back = dummy

        while n:
            forward = forward.next
            # why do you always forget decrease n????? why!!!!!!!
            n -= 1

        while forward.next:
            back = back.next
            forward = forward.next

        back.next = back.next.next

        return dummy.next