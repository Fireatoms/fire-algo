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
        post = encounter_node
        while pre != post:
            pre = pre.next
            post = post.next

        return pre

    def get_encounter_node(self, head):
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return slow

        return None