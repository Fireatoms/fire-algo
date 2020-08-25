# link: https://leetcode.com/problems/insertion-sort-list/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        # Introduce dummy node to simplify insertion
        dummy = ListNode(0)
        dummy.next = head
        ordered_tail = head
        while ordered_tail and ordered_tail.next:
            node_to_insert = ordered_tail.next
            pre = dummy
            if ordered_tail.val > node_to_insert.val:
                while pre.next.val <= node_to_insert.val:
                    pre = pre.next
                ordered_tail.next = node_to_insert.next
                node_to_insert.next = pre.next
                pre.next = node_to_insert
            else:
                ordered_tail = ordered_tail.next
        return dummy.next

def insertion_sort(arr):
    for j in range(1, len(arr)):
        val = arr[j]
        i = j - 1
        while i >= 0:
            if arr[i] > val:
                arr[i+1] = arr[i]
            else:
                break
            i -= 1
        arr[i+1] = val


if __name__ == "__main__":
    arr = [i for i in range(10, -1, -1)]
    insertion_sort(arr)
    print(arr)