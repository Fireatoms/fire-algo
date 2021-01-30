# link: https://leetcode-cn.com/problems/shan-chu-lian-biao-de-jie-dian-lcof/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        while head:
            if head.val == val:
                pre.next = head.next
            pre = head
            head = head.next
        return dummy.next

    def print_list(self, head):
        order = []
        while head:
            order.append(head.val)
            head = head.next
        print('=>'.join(map(str, order)))


if __name__ == "__main__":
    head = ListNode(4)
    head.next = ListNode(5)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(9)
    sl = Solution()
    sl.print_list(head)
    sl.deleteNode(head, 9)
    sl.print_list(head)