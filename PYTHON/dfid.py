
open_list = []
parent = {}
closed_list = []

def print_path(start, goal):
    cur = parent[goal]
    print(goal)
    while cur != start:
        print(cur)
        cur = parent[cur]
    print(cur)

def dfs(g, depth, max_depth, current, goal):
    if current == goal:
        closed_list.append(open_list.pop())
        print("Goal found ", current)
        print_path("a", goal)
        print("Depth: ", depth)
        print("Max Depth: ", max_depth)
        print(open_list)
        print(closed_list)
        return


    if depth == max_depth:
        return
    
    if not g.get(current):
        return
    for neighbour in g[current]:
        if neighbour not in closed_list:
            open_list.append(neighbour)
            parent[neighbour] = current
            dfs(g, depth + 1, max_depth, neighbour, goal)
            open_list.pop()
            closed_list.append(neighbour)

def dfid(g, max_depth, start, goal):
    for i in range(1, max_depth + 1):
        global open_list
        global closed_list
        global parent
        open_list = []
        closed_list = []
        parent = {}
        open_list.append(start)
        dfs(g, 1, i, start, goal)

g = {
    "a": ["b", "c"],
    "b": ["d", "e"],
    "c": ["f", "g"],
    "d": ["h", "i"],
    "e": ["j", "k"],
    "f": ["l", "m"],
    "g": ["n", "z"]
}

start = "a"
goal = "z"

dfid(g, 4, start, goal)