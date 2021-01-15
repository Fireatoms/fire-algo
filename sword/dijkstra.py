class Solution:
    def __init__(self, graph, s, t):
        self.INFINITY = float('inf')
        self.graph = graph
        self.s = s
        self.t = t
        self.cost, self.prev = self.init_cost_prev()
        self.processed = {t}

    def init_cost_prev(self):
        cost = {self.s: 0}
        prev = {}
        for t, tv in self.graph[self.s].items():
            cost[t] = tv
            prev[t] = self.s
        for p in self.graph:
            if p not in cost:
                cost[p] = self.INFINITY
        return cost, prev

    def get_least_cost_node(self):
        least_cost = self.INFINITY
        least_cost_node = ""
        for node, node_cost in self.cost.items():
            if node not in self.processed and node_cost < least_cost:
                least_cost = node_cost
                least_cost_node = node
        return least_cost_node

    def dijkstra(self):
        least_cost_node = self.get_least_cost_node()
        while least_cost_node != "":
            for next_node, next_node_cost in self.graph[least_cost_node].items():
                new_cost = self.cost[least_cost_node] + next_node_cost
                if new_cost < self.cost[next_node]:
                    self.cost[next_node] = new_cost
                    self.prev[next_node] = least_cost_node
                self.processed.add(least_cost_node)
            least_cost_node = self.get_least_cost_node()


    def print_path(self, s, t, prev):
        if s != t:
            self.print_path(s, prev[t], prev)
        print(t)
        # print(t)
        # if s == t:
        #     return
        # self.print_path(s, prev[t], prev)


if __name__ == "__main__":
    graph = {
        'a': {
            'b': 5,
            'c': 0
        },
        'b': {
            'e': 15,
            'f': 20
        },
        'c': {
            'e': 30,
            'f': 35
        },
        'e': {
            'g': 20
        },
        'f': {
            'g': 10
        },
        'g': {

        }
    }
    sl = Solution(graph, "a", "g")
    sl.dijkstra()
    sl.print_path(sl.s, sl.t, sl.prev)