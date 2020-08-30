# link: https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None

        mid = self.find_mid(head)
        node = TreeNode(mid.val)

        # this means head has not sub tree
        if head == mid:
            return node

        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(mid.next)
        return node

    def find_mid(self, head):
        pre = None
        slow = head
        fast = head

        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next

        if pre:
            pre.next = None

        return slow
