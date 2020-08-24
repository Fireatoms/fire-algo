# link: https://leetcode.com/problems/partition-list/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummy_little = ListNode(0)
        dummy_large = ListNode(0)
        little_cur = dummy_little
        large_cur = dummy_large

        cur = head
        while cur:
            if cur.val < x:
                little_cur.next = cur
                little_cur = little_cur.next
            else:
                large_cur.next = cur
                large_cur = large_cur.next
            cur = cur.next

        large_cur.next = None
        little_cur.next = dummy_large.next

        return dummy_little.next


def print_list(head):
    while head:
        print(head.val)
        head = head.next


if __name__ == "__main__":
    cur = head = ListNode(1)
    cur.next = ListNode(4)
    cur.next.next = ListNode(3)
    cur.next.next.next = ListNode(2)
    cur.next.next.next.next = ListNode(5)
    cur.next.next.next.next.next = ListNode(2)
    sl = Solution()
    hl = sl.partition(head, 3)
    print_list(hl)

