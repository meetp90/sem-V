# dfs in python
graph = {
    'S': ['A', 'B'],
    'A': ['C', 'D'],
    'B': ['F', 'G'],
    'D': [],
    'C': [],
    'F': [],
    'G': []
}
def dfs(graph, start, goal):
    stack = [(start, [start])]
    visited = set()
    while stack:
        (vertex, path) = stack.pop()
        print(vertex)
        if vertex not in visited:
            if vertex == goal:
                return path
            visited.add(vertex)
            for neighbor in graph[vertex]:
                stack.append((neighbor, path + [neighbor]))

print(dfs(graph,'S','G'))
