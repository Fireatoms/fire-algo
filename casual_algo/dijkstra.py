INFINITY = float('inf')

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

# Do not record source node
cost = {
    'a': INFINITY,
    'b': 5,
    'c': 0,
    'e': INFINITY,
    'f': INFINITY,
    'g': INFINITY
}

processed = set()

prev = {
    'a': None,
    'b': 'a',
    'c': 'a',
    'e': None,
    'f': None,
    'g': None
}


def find_least_node(cost, processed):
    lowest_cost = INFINITY
    least_node = None
    for key in cost:
        if key not in processed and cost[key] < lowest_cost:
            # I have forgotten this!!!!
            lowest_cost = cost[key]
            least_node = key
    return least_node


def dijk(graph, cost, processed, prev):
    least_node = find_least_node(cost, processed)
    while least_node:
        next_nodes = graph[least_node]
        for next_node, next_cost in next_nodes.items():
            new_cost = cost[least_node] + next_cost
            if new_cost < cost[next_node]:
                cost[next_node] = new_cost
                prev[next_node] = least_node

        processed.add(least_node)

        least_node = find_least_node(cost, processed)


def print_path(prev, s, t):
    if s != t:
        print_path(prev, s, prev[t])
    print(t)


if __name__ == "__main__":
    dijk(graph, cost, processed, prev)
    print_path(prev, 'a', 'g')