# link: https://leetcode-cn.com/problems/reverse-nodes-in-k-group/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        pre = dummy
        while head:
            tail = pre
            for i in range(k):
                tail = tail.next
                if not tail:
                    return dummy.next

            tail_next = tail.next
            head, tail = self.reverse_list(head, tail)
            pre.next = head
            tail.next = tail_next
            pre = tail
            head = tail.next

        return dummy.next

    def reverse_list(self, head, tail):
        pre = tail.next
        cur = head
        # while cur: # rely on tail.next = None, bad!
        while pre != tail:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return tail, head