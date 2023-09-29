#single source shortest path

import heapq

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))

def dijkstra(graph, src):
    distances = [float('inf')] * graph.V
    distances[src] = 0
    visited = [False] * graph.V
    min_heap = [(0, src)]

    while min_heap:
        dist_u, u = heapq.heappop(min_heap)

        if visited[u]:
            continue

        visited[u] = True

        for v, weight in graph.graph[u]:
            if not visited[v] and distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
                heapq.heappush(min_heap, (distances[v], v))

    return distances

g = Graph(5)
g.add_edge(0, 1, 2)
g.add_edge(0, 3, 4)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 1)
g.add_edge(2, 4, 2)
g.add_edge(3, 4, 3)

src_vertex = 0
shortest_distances = dijkstra(g, src_vertex)

print("Shortest distances from source vertex", src_vertex)
for i, dist in enumerate(shortest_distances):
    print(f"Vertex {i}: {dist}")
