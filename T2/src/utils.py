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

def get_fib_p():
    fib_fp = open("experimentos/files/find_p_fib.json")
    fib_p = json.load(fib_fp)
    fib_fp.close()
    return fib_p

def get_bin_p():
    bin_fp = open("experimentos/files/find_p_bin.json")
    bin_p = json.load(bin_fp)
    bin_fp.close()
    return bin_p

def get_fib_v():
    fib_fp = open("experimentos/files/find_v_fib.json")
    fib_v = json.load(fib_fp)
    fib_fp.close()
    return fib_v

def get_bin_v():
    bin_fp = open("experimentos/files/find_v_bin.json")
    bin_v = json.load(bin_fp)
    bin_fp.close()
    return bin_v

def get_min_p():
    fib_p = get_fib_p()
    bin_p = get_bin_p()
    dict_xd = {}
    for i in fib_p.keys():
        current = float(fib_p[i]["time_std"]) + float(bin_p[i]["time_std"])
        dict_xd[float(i)] = current
    index = max(sorted(dict_xd.items())[0:3])[0]
    return index