//minimum spanning tree

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

def kruskal_mst(graph):
    graph.graph = sorted(graph.graph, key=lambda item: item[2])
    result = []
    parent = []
    
    def find_parent(i):
        if parent[i] == -1:
            return i
        if parent[i] != -1:
            return find_parent(parent[i])

    def union(u, v):
        root_u = find_parent(u)
        root_v = find_parent(v)
        parent[root_u] = root_v

    parent = [-1] * graph.V

    for i in range(graph.V - 1):
        u, v, w = graph.graph[i]
        root_u = find_parent(u)
        root_v = find_parent(v)

        if root_u != root_v:
            result.append([u, v, w])
            union(root_u, root_v)

    return result

g = Graph(4)
g.add_edge(0, 1, 10)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 4)

mst = kruskal_mst(g)
print("Edges in MST:")
for u, v, weight in mst:
    print(f"{u} - {v} : {weight}")
