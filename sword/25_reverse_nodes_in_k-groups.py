# link: https://leetcode-cn.com/problems/reverse-nodes-in-k-group/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        pre = dummy

        while head:
            tail = head
            for i in range(k - 1):
                tail = tail.next
                if not tail:
                    return dummy.next
            new_head, new_tail = self.reverse(head, tail)
            pre.next = new_head
            pre = new_tail
            head = pre.next
        return dummy.next

    def reverse(self, head, tail):
        pre = tail.next
        cur = head
        while pre != tail:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return tail, head