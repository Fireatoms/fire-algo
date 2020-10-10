# link: https://leetcode.com/problems/merge-k-sorted-lists/
import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        node_heap = [(node.val, i) for i, node in enumerate(lists) if node]
        heapq.heapify(node_heap)

        head = cur = ListNode()
        while node_heap:
            heap_top = heapq.heappop(node_heap)
            cur.next = ListNode(heap_top[0])
            cur = cur.next

            if lists[heap_top[1]].next:
                lists[heap_top[1]] = lists[heap_top[1]].next
                heapq.heappush(node_heap, (lists[heap_top[1]].val, heap_top[1]))

        return head.next


class Solution1:
    """
    their exists a solution can reduce the space complexity to o(1)
    link: https://leetcode.com/problems/merge-k-sorted-lists/solution/
    """
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # devide and conquer
        if not lists:
            return
        # It is necessary for stopping recursion
        if len(lists) == 1:
            return lists[0]
        mid = len(lists) // 2
        l = self.mergeKLists(lists[:mid])
        r = self.mergeKLists(lists[mid:])
        return self.merge(l, r)

    def merge(self, l, r):
        dummy = cur = ListNode(0)
        while l and r:
            if l.val <= r.val:
                cur.next = l
                l = l.next
            else:
                cur.next = r
                r = r.next
            cur = cur.next

        cur.next = l or r
        return dummy.next