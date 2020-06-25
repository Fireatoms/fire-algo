# graph storage
# dfs bfs
from collections import deque


class Graph:
    """undirected graph"""
    def __init__(self, ver_num):
        self.ver_num = ver_num
        self.adj = [[] for _ in range(ver_num)]
        self.found = False

    def add_edge(self, s, t):
        self.adj[s].append(t)
        self.adj[t].append(s)

    def bfs(self, s, t):
        queue = deque()
        visited = [False for _ in range(self.ver_num)]
        prev = [-1 for _ in range(self.ver_num)]
        queue.append(s)
        visited[s] = True

        while queue:
            ver = queue.popleft()
            for ver_con in self.adj[ver]:
                if not visited[ver_con]:
                    visited[ver_con] = True
                    prev[ver_con] = ver
                    if ver_con == t:
                        self.print_recur(prev, s, t)
                        return

                    queue.append(ver_con)

    def dfs(self, s, t):
        prev = [-1 for _ in range(self.ver_num)]
        visited = [False for _ in range(self.ver_num)]

        self.dfs_recur(visited, prev, s, t)
        self.print_recur(prev, s, t)

    def dfs_recur(self, visited, prev, s, t):
        if self.found:
            return

        visited[s] = True
        if s == t:
            self.found = True
            return

        for ver in self.adj[s]:
            if not visited[ver]:
                prev[ver] = s
                self.dfs_recur(visited, prev, ver, t)

    def dfs_iter(self, s, t):
        graph_stack = []
        visited = [False for _ in range(self.ver_num)]
        prev = [-1 for _ in range(self.ver_num)]

        graph_stack.append(s)
        visited[s] = True

        while graph_stack:
            ver = graph_stack.pop()
            for ver_con in self.adj[ver]:
                if not visited[ver_con]:
                    visited[ver_con] = True
                    prev[ver_con] = ver
                    if ver_con == t:
                        self.print_recur(prev, s, t)
                        return

                    graph_stack.append(ver_con)

    def print_recur(self, prev, s, t):
        if s != t and prev[t] != -1:
            self.print_recur(prev, s, prev[t])

        print(" {}".format(t))


def construct_graph():
    graph = Graph(8)
    graph.add_edge(0, 1)
    graph.add_edge(0, 3)
    graph.add_edge(1, 2)
    graph.add_edge(1, 4)
    graph.add_edge(3, 4)
    graph.add_edge(2, 5)
    graph.add_edge(4, 5)
    graph.add_edge(4, 6)
    graph.add_edge(5, 7)
    graph.add_edge(6, 7)

    return graph


def print_recur(prev, s, t, path):
    if s == t or prev[t] == -1:
        path.append(t)
        return

    print_recur(prev, s, prev[t], path)
    path.append(t)


def print_recur_1(prev, s, t, path):
    if s != t and prev[t] != -1:
        print_recur_1(prev, s, prev[t], path)

    path.append(t)


def print_iter(prev, s, t):
    path = []
    while t != s and t != -1:
        path.insert(0, t)
        t = prev[t]

    path.insert(0, t)
    print(path)


if __name__ == "__main__":
    graph = construct_graph()
    graph.dfs_iter(0, 6)
    # graph.dfs(0, 6)
    # graph.bfs(0, 6)
    # prev = [-1, 0, 2, 1, 3, 4]
    # path = []
    # print_recur_1(prev, 0, 5, path)
    # print(path)
    # print_iter(prev, 0, 5)