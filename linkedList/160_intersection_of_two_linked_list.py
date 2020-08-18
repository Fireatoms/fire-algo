# link: https://leetcode.com/problems/intersection-of-two-linked-lists/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None or headB is None:
            return None

        A_pointer = headA
        B_pointer = headB

        while A_pointer != B_pointer:
            A_pointer = A_pointer.next if A_pointer else headB
            B_pointer = B_pointer.next if B_pointer else headA

        return A_pointer

class SolutionHash:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        node_set = set()
        while headA:
            node_set.add(headA)
            headA = headA.next

        while headB:
            if headB in node_set:
                return headB
            headB = headB.next

        return None

class SolutionBruteForce:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        while headA:
            p = headB
            while p:
                if headA == p:
                    return headA
                else:
                    p = p.next

            headA = headA.next

        return None


if __name__ == "__main__":
    cur = ListNode(0)
    cur.next = ListNode(1)
    node_set = set()
    node_set.add(cur)
    node_set.add(cur.next)
    print(node_set)
    print(type(node_set.pop()))
