def dijkstra(graph, start, queue):
    distances = {}
    for node in graph:
        distances[node] = float('infinity')
        queue.insert(node, float('infinity'))
    distances[start] = 0
    queue.decrease_key(start, 0)
    while not queue.empty():
        current_node, current_distance = queue.extract_min()
        if not current_distance > distances[current_node]:
            for neighbor, weight in graph[current_node].items():
                distance = current_distance + weight;
                if distances[neighbor] > distance:
                    distances[neighbor] = distance
                    queue.decrease_key(neighbor, distance)
    return " ".join([str(n) for n in distances.values()])

"""
Input de prueba

6 10
1 2 2
1 6 8
1 3 1
2 3 6
2 5 3
2 6 5
3 4 2
3 5 4
4 5 7
5 6 1
1

Output

0 2 1 3 5 6
"""



