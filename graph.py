# graph
# dfs
# bfs
# assume value of all vertices is consecutive to simply operation
from collections import deque


class Graph:
    def __init__(self, v):
        """
        1. the vertice num
        2. list for storing vertices connecting to current vertice
        """
        self.vertice_num = v
        self.adj = [[] for _ in range(v)]

    def add_edge(self, s, t):
        # undirected graph
        self.adj[s].append(t)
        self.adj[t].append(s)

    def bfs(self, s, t):
        # initialize auxiliary data structure
        queue = deque()
        visted = [False for _ in range(self.vertice_num)]
        prev = [-1 for _ in range(self.vertice_num)]

        queue.append(s)
        visted[s] = True

        while queue:
            ver = queue.popleft()
            for ver_con in self.adj[ver]:
                if not visted[ver_con]:
                    prev[ver_con] = ver
                    visted[ver_con] = True
                    if ver_con == t:
                        self.print_path(prev, s, t)
                        return
                    queue.append(ver_con)

    def print_path(self, prev, s, t):
        if prev[t] != -1 and s != t:
            self.print_path(prev, s, prev[t])

        print(" {}".format(t))


def construct_graph():
    graph = Graph(8)
    graph.adj[0] = [1, 3]
    graph.adj[1] = [0, 2, 4]
    graph.adj[2] = [1, 5]
    graph.adj[3] = [0, 4]
    graph.adj[4] = [1, 3, 5, 6]
    graph.adj[5] = [2, 4, 7]
    graph.adj[6] = [4, 7]
    graph.adj[7] = [5, 6]

    return graph


if __name__ == "__main__":
    graph = construct_graph()
    graph.bfs(0, 6)