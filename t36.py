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
        return 0
    
    dist = [None] * (max(graph) + 1)
    dq = deque()
    dq.append(start)
    dist[start] = 0

    while dq:
        v1 = dq.popleft()
        dist1 = dist[v1]
        for v2 in graph[v1]:
            # print(f"{v1=}, {v2=}", file=sys.stderr)
            if v2 == end:
                return dist1 + 1

            dist2 = dist[v2]
            if dist2 is None or dist2 > dist1:
                dq.append(v2)
                dist[v2] = dist1 + 1
    
    return -1

ans = solve(graph, start, end)
print(ans)