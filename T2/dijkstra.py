import priorityQueue as queue
import sys

def dijkstra(graph, start, queue):
    distances = {}
    for node in graph:
        distances[node] = float('infinity')
        queue.insert(node, float('infinity'))
    distances[start] = 0
    queue.decrease_key(start, 0)
    while not queue.empty():
        current_node, current_distance = queue.extract_min()
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight;
            if distances[neighbor] > distance:
                distances[neighbor] = distance
                queue.decrease_key(neighbor, distance)
    return " ".join([str(n) for n in distances.values()])

def dijkstra_controller():
    graph = {}
    vertices, aristas = list(map(int, input().split()))
    for i in range(vertices):
        graph[i+1] = {}
    for i in range(aristas):
        u, v, s = list(map(int, input().split()))
        graph[u][v] = s
        graph[v][u] = s
    print(graph)
    start = int(input())
    if sys.argv[1] == "FibonacciHeap":
        queuexd = queue.FibonacciHeap()
    else:
        queuexd = queue.BinaryHeap()
    print(dijkstra(graph, start, queuexd))
     
dijkstra_controller()


"""
El grafo deberia tener la siguiente forma:

{
    'U': {'V': 2, 'W': 5, 'X': 1},
    'V': {'U': 2, 'X': 2, 'W': 3},
    'W': {'V': 3, 'U': 5, 'X': 3, 'Y': 1, 'Z': 5},
    'X': {'U': 1, 'V': 2, 'W': 3, 'Y': 1},
    'Y': {'X': 1, 'W': 1, 'Z': 1},
    'Z': {'W': 5, 'Y': 1},
}

Es decir un diccionario, cuyas key sean los elementos y cuyo valor
sea otro dict que tendrá por key el nodo con el que conecta y como valor
el peso que hay.
"""


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
