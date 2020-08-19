# link: https://leetcode.com/problems/reorder-list/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find middle node
        if head is None:
            return

        head_pos = head

        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None

        # reverse linked list from middle node
        pre = None
        cur = mid
        while cur:
            third = cur.next
            cur.next = pre
            pre = cur
            cur = third

        # insert node
        mid_begin = pre
        while mid_begin:
            forward_next = head_pos.next
            back_next = mid_begin.next
            head_pos.next = mid_begin
            mid_begin.next = forward_next
            head_pos = forward_next
            mid_begin = back_next

        return head


def print_list(head):
    while head:
        print(head.val)
        head = head.next


if __name__ == "__main__":
    head = ListNode(0)
    head_pos = head
    for i in range(1, 6):
        head.next = ListNode(i)
        head = head.next

    sl = Solution()
    sl.reorderList(head_pos.next)