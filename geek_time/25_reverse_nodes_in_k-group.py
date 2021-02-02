# link: https://leetcode-cn.com/problems/reverse-nodes-in-k-group/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if self.if_terminated(head, k):
            return head

        tail = head
        for i in range(k - 1):
            tail = tail.next

        new_head, new_tail = self.reverse_nodes(head, tail)
        new_tail.next = self.reverseKGroup(new_tail.next, k)
        return new_head

    def if_terminated(self, head, k):
        if not head:
            return True

        for i in range(k - 1):
            head = head.next
            if not head:
                return True

        return False


    def reverseKGroupIter(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode()
        dummy.next = head

        pre = dummy
        while head:
            tail = head
            for i in range(k - 1):
                tail = tail.next
                if not tail:
                    return dummy.next

            new_head, new_tail = self.reverse_nodes(head, tail)
            pre.next = new_head
            pre = new_tail
            head = pre.next

        return dummy.next

    def reverse_nodes(self, head, tail):
        pre = tail.next
        cur = head

        while pre != tail:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp

        return tail, head


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    sl = Solution()
    head = sl.reverseKGroupIter(head, 2)
    print(head)