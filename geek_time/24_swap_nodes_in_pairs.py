# link: https://leetcode-cn.com/problems/swap-nodes-in-pairs/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        new_head = head.next
        head.next = self.swapPairs(head.next.next)
        new_head.next = head
        return new_head

    def swapPairsIter(self, head: ListNode) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        prepre = dummy
        while prepre.next and prepre.next.next:
            pre, cur = prepre.next, prepre.next.next
            pre.next = cur.next
            cur.next = pre
            prepre.next = cur
            prepre = pre

        return dummy.next

    def swapPairsOrigin(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        dummy = ListNode()
        prepre, pre, cur = dummy, head, head.next
        while cur:
            pre, cur = self.swap_two_nodes(pre, cur)
            prepre.next = pre

            prepre = cur
            pre = cur.next
            cur = pre.next if pre is not None else None

        return dummy.next

    def swap_two_nodes(self, pre, cur):
        tmp = cur.next
        cur.next = pre
        pre.next = tmp

        return cur, pre
