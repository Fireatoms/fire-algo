# link: https://leetcode.com/problems/insertion-sort-list/

# 核心思想：
# 1. 数据分为已排序和待排序，记录已排序数据的尾结点。进一步根据这个结点找到下一个待插入的结点
# 2. 利用链表插入的便利性，只需要在已排序数据中找到新数据的插入位置即可。
# 3. 小技巧：自行引入哨兵头结点，简化结点插入操作

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head):
        # 为了插入方便，增加哨兵头结点
        sentry = ListNode(-1)
        sentry.next = head
        sorted_tail_node = head
        while sorted_tail_node and sorted_tail_node.next:
            node_to_insert = sorted_tail_node.next
            # 从已排序结点中找到的新结点的插入位置
            node_to_insert_pre = sentry
            # 尾部判断是否需要下面的遍历找插入点的操作，提高效率
            if sorted_tail_node.val > node_to_insert.val:
                # 从已排序结点中找插入位置, 判断条件写上=的目的：保持原序列的稳定，也即两个相等数据排序后前后顺序不变
                # 如果不需要保持稳定，循环条件可以写成 while node_to_insert_pre.next.val < node_to_insert.val
                while node_to_insert_pre.next.val <= node_to_insert.val:
                    node_to_insert_pre = node_to_insert_pre.next
                sorted_tail_node.next = node_to_insert.next
                node_to_insert.next = node_to_insert_pre.next
                node_to_insert_pre.next = node_to_insert
            else:
                sorted_tail_node = sorted_tail_node.next

        return sentry.next

