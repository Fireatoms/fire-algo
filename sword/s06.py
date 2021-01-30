# link: https://leetcode-cn.com/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof/
from typing import List
from collections import deque


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        assist_stack = []
        ans = []
        while head:
            assist_stack.append(head)
            head = head.next
        while assist_stack:
            node = assist_stack.pop()
            ans.append(node.val)
        return ans

    def reversePrintQueue(self, head: ListNode) -> List[int]:
        ans = deque()
        while head:
            ans.appendleft(head.val)
            head = head.next
        return list(ans)


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(3)
    head.next.next = ListNode(2)
    sl = Solution()
    print(sl.reversePrint(head))