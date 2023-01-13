opened = []
closed = []

def bfs(graph, start, goal):
    opened.append(start)
    while opened:
        print("open list = ",end="")
        print(opened)
        print("close list = ",end="")
        print(closed)
        node = opened.pop(0)
        if node == goal:
            print("found")
            closed.append(goal)
            return True
        if node not in closed:
            closed.append(node)
            opened.extend(graph[node])
    return False


graph = {
    'S': ['A', 'B'],
    'A': ['C', 'D'],
    'B': ['F', 'G'],
    'D': [],
    'C': [],
    'F': [],
    'G': []
}
print(bfs(graph, 'S', 'G'))
print("open list = ",end="")
print(opened)
print("close list = ",end="")
print(closed)


# graph = {
#         '1': ['2', '3', '4'],
#         '2': ['5', '6'],
#         '5': ['9', '10'],
#         '4': ['7', '8'],
#         '7': ['11', '12']
#         }

# def backtrace(parent, start, end):
#     path = [end]
#     while path[-1] != start:
#         path.append(parent[path[-1]])
#     path.reverse()
#     return path
        

# def bfs(graph, start, end):
#     parent = {}
#     queue = []
#     queue.append(start)
#     while queue:
#         node = queue.pop(0)
#         if node == end:
#             return backtrace(parent, start, end)
#         for adjacent in graph.get(node, []):
#             if node not in queue :
#                 parent[adjacent] = node 
#                 queue.append(adjacent)

# print(bfs(graph, 'S', 'G'))