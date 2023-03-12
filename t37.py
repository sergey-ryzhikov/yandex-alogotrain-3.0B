n = int(input())
graph = {(x+1):set() for x in range(n)}

for i in range(n):
    vals = list(map(int,input().split()))
    for j, val in enumerate(vals):
        if val:
            graph[i+1].add(j+1)
            graph[j+1].add(i+1)
start, end = map(int, input().split())

# ====
from collections import deque
import sys

def solve(graph, start, end):
    if start == end:
        return 0, []
    
    dist = [None] * (max(graph) + 1)
    dq = deque()
    dq.append(start)
    dist[start] = 0

    ret = None
    while dq:
        v1 = dq.popleft()
        dist1 = dist[v1]
        for v2 in graph[v1]:
            # print(f"{v1=}, {v2=}", file=sys.stderr)
            if v2 == end:
                ret = dist1 + 1
                dq.clear()
                break

            dist2 = dist[v2]
            if dist2 is None or dist2 > dist1:
                dq.append(v2)
                dist[v2] = dist1 + 1
    
    if ret is None:
        return None, []
    
    x = ret
    v1 = end
    backpath = [end]

    while x > 0:
        for v2 in graph[v1]:
            if dist[v2] == x - 1:
                backpath.append(v2)
                break
        else:
            raise RuntimeError(f'missing parent for {v2}')

        v1 = v2
        x -= 1

    return ret, backpath

ans, backpath = solve(graph, start, end)
if ans is None:
    print(-1)
elif ans == 0:
    print(ans)
else:
    print(ans)
    print(*reversed(backpath))