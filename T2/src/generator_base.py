import random

def decision(p):
    return random.uniform(0, 1 + 1e-9) < p

def add_directed_edge(graph, i, j, edge_weight):
    new_edge = {j: edge_weight}
    if graph.get(i) is None:
        graph[i] = new_edge
    else:
        graph[i].update(new_edge)

def add_edge(graph, i, j, weight):
    add_directed_edge(graph, i, j, weight)
    add_directed_edge(graph, j, i, weight)

def generator(nodes, density):
    graph = {}
    total_nodes = 0
    nodes_out = []
    for i in range(1, nodes):
        edge_weight = random.randint(1, 10**9)
        add_edge(graph, i, i+1, edge_weight)
        nodes_out.append(' '.join([str(i), str(i+1), str(edge_weight)]))
        total_nodes += 1
    for i in range(1, nodes-1):
        for j in range(i+2, nodes+1):
            if decision(density):
                edge_weight = random.randint(1, 10**9)
                add_edge(graph, i, j, edge_weight)
                nodes_out.append(' '.join([str(i), str(j), str(edge_weight)]))
                total_nodes += 1
    print(' '.join([str(nodes), str(total_nodes)]))
    for i in range(total_nodes):
        print(nodes_out[i])
    print(random.randint(1, nodes))
    return graph






                