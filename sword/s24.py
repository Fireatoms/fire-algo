# link: https://leetcode-cn.com/problems/fan-zhuan-lian-biao-lcof/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        pre = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre

    def print_list(self, head):
        order_list = []
        while head:
            order_list.append(head.val)
            head = head.next
        print('=>'.join(map(str, order_list)))


if __name__ == "__main__":
    dummy = ListNode(0)
    node = dummy
    for i in range(5):
        node.next = ListNode(i)
        node = node.next
    sl = Solution()
    sl.print_list(dummy.next)
    new_head = sl.reverseList(dummy.next)
    sl.print_list(new_head)