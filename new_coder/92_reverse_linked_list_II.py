# link: https://leetcode-cn.com/problems/reverse-linked-list-ii/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head

        i = 0
        pre = None
        cur = dummy
        m_pre, m_node, n_node, n_after = None, None, None, None
        while True:
            if i == m:
                m_pre = pre
                m_node = cur
            if i == n:
                n_node = cur
                n_after = cur.next
                break
            i += 1
            pre = cur
            cur = cur.next

        pre = n_after
        cur = m_node
        while pre != n_node:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp

        m_pre.next = n_node

        return dummy.next