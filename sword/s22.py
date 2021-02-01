# link: https://leetcode-cn.com/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        ahead = head
        after = head
        for i in range(k):
            ahead = ahead.next
        while ahead:
            ahead = ahead.next
            after = after.next
        return after

    def print_list(self, head):
        order_list = []
        while head:
            order_list.append(head.val)
            head = head.next
        print("=>".join(map(str, order_list)))


if __name__ == "__main__":
    sl = Solution()
    head = ListNode(0)
    cur = head
    for i in range(1, 6):
        cur.next = ListNode(i)
        cur = cur.next
    sl.print_list(head)
    last_node = sl.getKthFromEnd(head, 3)
    sl.print_list(last_node)