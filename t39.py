n = int(input())

arr = [[[None] * n for _ in range(n)] for _ in range(n)]

start = None
for i in range(n):
    input()  # empty line
    for j in range(n):
        line = input().strip()
        for k, ch in enumerate(line):
            if ch == '#': 
                continue
            elif ch == '.':
                arr[i][j][k] = 0
            elif ch == 'S':
                arr[i][j][k] = 0  # make no sence, but add for completeness
                start = (i,j,k)
            else:
                raise ValueError(f"{i=},{j=},{k=} '{ch}'")
# ===
from collections import deque

def solve(arr, start):
    n = len(arr)
    dq = deque()
    dq.append(start)

    graph = {start:0}

    steps = [(+1,0,0), (0,+1,0), (0,0,+1),
             (-1,0,0), (0,-1,0), (0,0,-1),
            ]

    while dq:
        i,j,k = dq.popleft()
        dist = graph[i,j,k]
        if i == 0:
            return dist

        for ni,nj,nk in ((i+si, j+sj, k+sk) for si,sj,sk in steps):
            if 0 <= ni < n and 0 <= nj < n and 0 <= nk < n:
                if arr[ni][nj][nk] == 0:
                    nijk = (ni,nj,nk)
                    if nijk not in graph :
                        graph[nijk] = dist + 1
                        dq.append(nijk)

print(solve(arr, start))