# link: https://leetcode-cn.com/problems/sort-list/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # terminal conditions
        if not head or not head.next:
            return head

        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None

        l = self.sortList(head)
        r = self.sortList(mid)
        # return the head of merged list
        # return the outermost node which is the answer we need
        return self.merge(l, r)

    def merge(self, l, r):
        # work well when both l and r are None
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

    @staticmethod
    def selection_sort(arr):
        length = len(arr)
        for i in range(length - 1):
            min_pos = i
            for j in range(i + 1, length):
                if arr[min_pos] > arr[j]:
                    min_pos = j
            arr[i], arr[min_pos] = arr[min_pos], arr[i]

    def sortListSelection(self, head: ListNode) -> ListNode:
        """
        time limited: 15/16
        :param head:
        :return:
        """
        if not head or not head.next:
            return head

        old_dummy = ListNode()
        old_dummy.next = head

        new_dummy = ListNode()
        new_cur = new_dummy

        while old_dummy.next:
            min_node_pre, pre_node = old_dummy, old_dummy
            min_node, cur_node = old_dummy.next, old_dummy.next

            while cur_node:
                if cur_node.val < min_node.val:
                    min_node = cur_node
                    min_node_pre = pre_node
                pre_node = cur_node
                cur_node = cur_node.next

            min_node_pre.next = min_node.next
            new_cur.next = min_node
            new_cur = new_cur.next

        new_cur.next = None
        return new_dummy.next


if __name__ == "__main__":
    sl = Solution()
    arr = [i for i in range(10, -1, -1)]
    sl.selection_sort(arr)
    print(arr)
