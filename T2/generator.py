import random
import sys

def pairs(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i != j:
                yield i, j

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

def generate_edges(graph, nodes, edges, density):
    for i, j in pairs(nodes):
        if random.randint(0, 1):
            add_edge(graph, i, j)
            edges += 1
            if edges >= density:
                break
    return graph, edges

def generator(nodes, density):
    graph = {}
    edges = 0
    while edges < density:
        graph, edges = generate_edges(graph, nodes, edges, density)
        print('edges', edges)
    return graph

generated_graph = generator(int(sys.argv[1]), int(sys.argv[2]))
for key, value in generated_graph.items():
    print(key, value)


                