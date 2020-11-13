import random

def decision(p):
    return random.uniform(0, 1 + 1e-9) < p

def add_directed_edge(graph, i, j, edge_weight):
    new_edge = {j: edge_weight}
    if graph.get(i) is None:
        graph[i] = new_edge
    else:
        graph[i].update(new_edge)

def add_edge(graph, i, j):
    edge_weight = random.randint(1, 10**9)
    add_directed_edge(graph, i, j, edge_weight)
    add_directed_edge(graph, j, i, edge_weight)

def generator(nodes, density):
    graph = {}
    for i in range(1, nodes):
        add_edge(graph, i, i+1)
    for i in range(1, nodes-1):
        for j in range(i+2, nodes+1):
            if decision(density):
                add_edge(graph, i, j)
    return graph






                