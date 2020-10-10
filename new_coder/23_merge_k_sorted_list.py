# link: https://leetcode-cn.com/problems/merge-k-sorted-lists/
import heapq
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        assist_queue = [(node.val, i) for i, node in enumerate(lists) if node]
        heapq.heapify(assist_queue)

        dummy = ListNode()
        cur = dummy

        while assist_queue:
            heap_top = heapq.heappop(assist_queue)
            cur.next = ListNode(heap_top[0])
            cur = cur.next

            if lists[heap_top[1]].next:
                heapq.heappush(assist_queue, (lists[heap_top[1]].next.val, heap_top[1]))
                lists[heap_top[1]] = lists[heap_top[1]].next

        return dummy.next

    def mergeKListsBottom(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None

        amount = len(lists)
        interval = 1

        while interval < amount:
            for i in range(0, amount - interval, 2 * interval):
                lists[i] = self.merge_two_lists(lists[i], lists[i + interval])
            interval *= 2

        return lists[0]

    def merge_two_lists(self, l, r):
        if not l or not r:
            return l or r

        dummy = ListNode()
        cur = dummy

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



if __name__ == "__main__":
    node1 = ListNode(1)
    node1.next = ListNode(2)

    arr = [node1]
    top = arr[0]
    top = top.next

    arr[0] = arr[0].next
    print('done')