# link: https://leetcode-cn.com/problems/copy-list-with-random-pointer/


"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def __init__(self):
        self.visited_nodes = {}

    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return None

        if head in self.visited_nodes:
            return self.visited_nodes[head]

        new_node = Node(head.val, None, None)
        self.visited_nodes[head] = new_node

        new_node.next = self.copyRandomList(head.next)
        new_node.random = self.copyRandomList(head.random)

        return new_node

    def get_clone_node(self, node):
        if node:
            if node in self.visited_nodes:
                return self.visited_nodes[node]
            else:
                clone_node = Node(node.val, None, None)
                self.visited_nodes[node] = clone_node
                return clone_node
        else:
            return None

    def copyRandomListIter(self, head: 'Node') -> 'Node':
        if not head:
            return head

        old_node = head
        new_node = Node(head.val, None, None)
        self.visited_nodes[old_node] = new_node

        while old_node:
            new_node.random = self.get_clone_node(old_node.random)
            new_node.next = self.get_clone_node(old_node.next)

            old_node = old_node.next
            new_node = new_node.next

        return self.visited_nodes[head]

    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head

        cur = head
        while cur:
            new_node = Node(cur.val, None, None)
            new_node.next = cur.next
            cur.next = new_node
            cur = cur.next.next

        cur = head
        while cur:
            cur.next.random = cur.random.next if cur.random else None
            cur = cur.next.next

        old_node = head
        new_node = head.next
        new_head = head.next
        while old_node:
            old_node.next = old_node.next.next
            new_node.next = new_node.next.next if new_node.next else None
            old_node = old_node.next
            new_node = new_node.next
        return new_head