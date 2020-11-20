import json

def graph_to_dict(d):
    g = d.split()
    graph = {}
    vertices, aristas = int(g[0]), int(g[1])
    for i in range(vertices):
        graph[i+1] = {}
    for i in range(aristas):
        index = 3*(i+1) - 1
        u, v, s = int(g[index]), int(g[index+1]), int(g[index+2])
        graph[u][v] = s
        graph[v][u] = s
    return graph

def get_aristas(graph):
    aristas = 0
    for node in graph.keys():
        for neighbor in graph[node].keys():
            aristas+=1
    return aristas//2

def log2_floor(n):
    ans = 0
    inc_aux = 1
    while inc_aux < n:
        inc_aux += inc_aux
        ans += 1
    if inc_aux == n:
        return ans
    return ans - 1

def log2_ceil(n):
    ans = 0
    inc_aux = 1
    while inc_aux < n:
        inc_aux += inc_aux
        ans += 1
    return ans
