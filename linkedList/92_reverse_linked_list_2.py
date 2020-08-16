# link: https://leetcode.com/problems/reverse-linked-list-ii/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        dummy_pos = dummy
        idx = 0
        head_pre = head
        while idx <= n:
            if idx == m:
                start_pre = head_pre
                start_pos = dummy
                pre = dummy
                cur = pre.next
                while idx < n and cur:
                    tmp = cur.next
                    cur.next = pre
                    pre = cur
                    cur = tmp
                    idx += 1
                start_pre.next = pre
                start_pos.next = cur

            idx += 1
            head_pre = dummy
            dummy = dummy.next

        return dummy_pos.next


def contruct_list():
    head = ListNode(1)
    head_pos = head
    for i in range(2, 3):
        head.next = ListNode(i)
        head = head.next

    return head_pos


def print_list(head):
    if head is None:
        return
    print(head.val)
    print_list(head.next)


if __name__ == "__main__":
    head = contruct_list()
    sl = Solution()
    head = sl.reverseBetween(head, 1, 2)
    print_list(head)