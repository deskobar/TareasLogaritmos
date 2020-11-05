import fq as queue
import sys

def dijkstra(graph, start, queue):
    distances = {}
    for node in graph:
        if node == start:
            queue.insert(start, 0)
            distances[start] = 0
        else:
            distances[node] = float('infinity')
            queue.insert(node, float('infinity'))
    while not queue.empty():
        current_node = queue.extract_min()
        current_node_val, current_distance = current_node.key, current_node.value
        if current_distance > distances[current_node_val]:
            continue
        for neighbor, weight in graph[current_node_val].items():
            distance = current_distance + weight;
            if distances[neighbor] > distance:
                distances[neighbor] = distance
                queue.decrease_key(neighbor, distance)
    return " ".join([str(n) for n in distances.values()])

graph = {1: {2: 2, 6: 8, 3: 1},
         2: {1: 2, 3: 6, 5: 3, 6: 5}, 
         3: {1: 1, 2: 6, 4: 2, 5: 4}, 
         4: {3: 2, 5: 7}, 
         5: {2: 3, 3: 4, 4: 7, 6: 1}, 
         6: {1: 8, 2: 5, 5: 1}}
         
print(dijkstra(graph, 1, queue.FibonacciHeap()))

        
    
