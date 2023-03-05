import sys

n_vert, n_edges = map(int, input().split())

graph = {}
for line in sys.stdin.readlines():
    line = line.strip()
    if line:  # FIX: empty lines in tests
        a,b = line.split()
        a,b = int(a), int(b)
        graph.setdefault(a,set()).add(b)
        graph.setdefault(b,set()).add(a)


def solve(graph, vertex=1):
    ret = [vertex]  # initial vertex always included
    if not graph:
        return ret

    nvert = max(graph.keys())
    visited = [False] * (nvert + 1)  # count from 1
    
    stack = [vertex]
    while stack:
        s = stack.pop()
        if visited[s]:
            continue
        visited[s] = True
        if s in graph:
            for xx in graph[s]:
                if not visited[xx]:
                    stack.append(xx)

    ret = [i for i,v in enumerate(visited) if v]
    return ret

ans = list(sorted(solve(graph, 1)))
print(len(ans))
print(*ans)