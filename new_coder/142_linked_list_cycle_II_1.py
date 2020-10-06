# link: https://leetcode-cn.com/problems/linked-list-cycle-ii/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        encounter_node = self.get_encounter_node(head)
        if not encounter_node:
            return None

        pre = head
        after = encounter_node
        while pre != after:
            pre = pre.next
            after = after.next

        return pre

    def get_encounter_node(self, head):
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return slow

        return None