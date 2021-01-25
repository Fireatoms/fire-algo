# link: https://leetcode-cn.com/problems/add-two-numbers/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        cur = dummy
        carry = 0

        while l1 or l2:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            val_sum = l1_val + l2_val + carry
            new_val = val_sum % 10
            carry = val_sum // 10
            cur.next = ListNode(new_val)
            cur = cur.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        if carry == 1:
            cur.next = ListNode(carry)
            cur = cur.next

        return dummy.next

    def sub_two_numbers(self, l1, l2):
        # length_l1 > length_l2
        dummy = ListNode()
        cur = dummy
        carry = 0
        is_positive = True

        while l1 or l2:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            sub_val = l1_val - l2_val + carry
            if sub_val < 0:
                carry = -1
                new_val = sub_val + 10
            else:
                carry = 0
                new_val = sub_val
            cur.next = ListNode(new_val)
            cur = cur.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        if carry == -1:
            is_positive = False
        return dummy.next, is_positive

    def print_list(self, head):
        order_list = []
        while head:
            order_list.append(head.val)
            head = head.next
        return "=>".join(map(str,order_list))


if __name__ == "__main__":
    head1 = ListNode(2)
    head2 = ListNode(5)
    head1.next = ListNode(4)
    head1.next.next = ListNode(3)
    head2.next = ListNode(6)
    head2.next.next = ListNode(4)

    sl = Solution()
    new_head, is_positive = sl.sub_two_numbers(head2, head1)
    print(sl.print_list(new_head), is_positive)