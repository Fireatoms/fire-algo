#link: https://leetcode.com/problems/palindrome-linked-list/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True

        mid = self.find_middle_node(head)
        seq_node = head

        # reverse linkedlist from mid
        pre = mid
        cur = mid.next
        pre.next = None
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        post_node = pre

        # compare positive ordered linked list and reversed linked list
        while seq_node is not None and post_node is not None:
            if seq_node.val != post_node.val:
                return False

            seq_node = seq_node.next
            post_node = post_node.next

        return True

    def find_middle_node(self, head):
        fast = slow = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow