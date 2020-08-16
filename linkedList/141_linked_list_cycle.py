# link: https://leetcode.com/problems/linked-list-cycle/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False

    def find_entry(self, head):
        slow = fast = head

        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                pre = head
                post = slow
                while pre != post:
                    pre = pre.next
                    post = post.next

                return pre.val

        return -1


if __name__ == "__main__":
    head = ListNode(0)
    n1 = ListNode(1)
    head.next = n1
    n1.next = ListNode(2)
    n1.next.next = ListNode(3)
    n1.next.next.next = n1
    sl = Solution()
    print(sl.find_entry(head))
