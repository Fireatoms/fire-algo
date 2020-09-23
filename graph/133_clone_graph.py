# link: https://leetcode.com/problems/clone-graph/
from collections import deque

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def __init__(self):
        self.visited = {}

    def cloneGraphDfs(self, node: 'Node') -> 'Node':
        if not node:
            return node

        if node in self.visited:
            return self.visited[node]

        clone_node = Node(node.val, [])
        self.visited[node] = clone_node

        if node.neighbors:
            clone_node.neighbors = [self.cloneGraphDfs(n) for n in node.neighbors]

        return clone_node

    def cloneGraphBfs(self, node: 'Node') -> 'Node':
        if not node:
            return node

        visited = {}

        que = deque([node])
        visited[node] = Node(node.val, [])

        while que:
            n = que.popleft()
            for neighbor in n.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val, [])
                    que.append(neighbor)

                visited[n].neighbors.append(visited[neighbor])

        return visited[node]



    def print_path(self, prev, s, t):
        if prev[t] != -1 and s != t:
            self.print_path(prev, s, prev[t])

        print(str(t) + ' ')


if __name__ == "__main__":
    sl = Solution()
    prev = [-1, 0, -1, -1, 1, -1, 4, -1]
    sl.print_path(prev, 0, 6)