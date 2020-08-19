# link: https://leetcode.com/problems/linked-list-cycle-ii/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # determine whether there is a ring
        slow = head
        fast = head

        has_cycle = False
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                has_cycle = True
                break

        if not has_cycle:
            return None

        cur = slow
        pre = head

        while cur != pre:
            cur = cur.next
            pre = pre.next

        return cur


if __name__ == "__main__":
    head = ListNode(3)
    head_pos = head
    head_pos.next = ListNode(2)
    head_entry = head_pos.next
    head_pos.next.next = ListNode(0)
    head_pos.next.next.next = ListNode(-4)
    head_pos.next.next.next.next = head_entry
    sl = Solution()
    print(sl.detectCycle(head).val)