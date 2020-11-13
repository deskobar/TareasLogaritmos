import priorityQueue as queue
import sys

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
        my_queue = queue.FibonacciHeap()
    else:
        my_queue = queue.BinaryHeap()
    print(dijkstra(graph, start, my_queue))
     
dijkstra_controller()