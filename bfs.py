graph = {
    '1': ['2', '3'],
    '2': ['4', '5'],
    '3': ['6'],
    '4': [],
    '5': ['6'],
    '6': []
}

visited = set()
queue = []

def bfs(visited, graph, node):
    visited.add(node)
    queue.append(node)

    while queue: 
        m = queue.pop(0)
        print(m, end=" ")

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

print("BFS is:")

bfs(visited, graph, '1')
