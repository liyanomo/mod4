inc = {
    1: [2, 5],
    2: [3, 4],
    3: [2],
    4: [2],
    5: [6, 7],
    6: [5],
    7: [8, 9],
    8: [7],
    9: [7],
}

visited = set()  
Q = [] 
BFS = []


def bfs(v):
    if v in visited:  
        return
    visited.add(v)  
    BFS.append(v) 
    for i in inc[v]:  
        if not i in visited:
            Q.append(i)
    while Q:
        bfs(Q.pop(0))

start = 1
bfs(start) 
print(BFS)  