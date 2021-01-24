# link: https://leetcode-cn.com/problems/reverse-linked-list/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre, cur = None, head
        while cur is not None:
            # not recommended
            cur.next, cur, pre = pre, cur.next, cur
            # tmp = cur.next
            # cur.next = pre
            # pre = cur
            # cur = tmp
        return pre

    def print_list(self, head):
        while head is not None:
            print(head.val)
            head = head.next


if __name__ == "__main__":
    head = ListNode(1)
    cur = head
    for i in range(2, 6):
        cur.next = ListNode(i)
        cur = cur.next
    sl = Solution()
    sl.print_list(head)
    new_head = sl.reverseList(head)
    sl.print_list(new_head)

