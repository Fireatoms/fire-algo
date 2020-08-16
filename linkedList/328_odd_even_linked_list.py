# link: https://leetcode.com/problems/odd-even-linked-list/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        odd = ListNode(0)
        even = ListNode(0)
        odd_head = odd
        even_head = even
        is_odd = True

        while head:
            if is_odd:
                odd.next = head
                odd = odd.next
            else:
                even.next = head
                even = even.next
            head = head.next
            is_odd = not is_odd

        even.next = None
        odd.next = even_head.next
        return odd_head.next

# not concise and wrong
# class Solution:
#     def oddEvenList(self, head: ListNode) -> ListNode:
#         index = 0
#         odd_head = ListNode(0)
#         odd_node = ListNode(0)
#         odd_tail = ListNode(0)
#         even_head = ListNode(0)
#         even_node = ListNode(0)
#         even_tail = ListNode(0)
#
#         while head:
#             index += 1
#             if index % 2 == 1:
#                 if index == 1:
#                     odd_head = head
#                     odd_node = head
#                     head = head.next
#                     continue
#                 odd_node.next = head
#                 odd_node = odd_node.next
#                 odd_tail = odd_node
#             else:
#                 if index % 2 == 0:
#                     even_head = head
#                     even_node = head
#                     head = head.next
#                     continue
#                 even_node.next = head
#                 even_node = even_node.next
#                 even_tail = even_node
#
#             head = head.next
#
#         even_tail.next = None
#         odd_tail.next = even_head
#         return odd_head
