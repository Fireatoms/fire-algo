# link: https://leetcode-cn.com/problems/linked-list-cycle/
import time

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow, fast = head, head
        while slow and fast and fast.next and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False

    def hasCycleSet(self, head: ListNode) -> bool:
        set_cache = set()
        while head:
            if head in set_cache:
                return True
            set_cache.add(head)
            head = head.next

        return False

    def hasCycleDirect(self, head: ListNode) -> bool:
        start_time = time.time()
        while head:
            head = head.next
            if time.time() - start_time >= 0.5:
                return True

        return False


def test_cycle():
    node1 = ListNode(1)
    node1.next = ListNode(2)
    node1.next.next = ListNode(3)
    node1.next.next.next = ListNode(4)
    node1.next.next.next.next = node1.next
    sl = Solution()
    print(sl.hasCycle(node1))


if __name__ == "__main__":
    test_cycle()