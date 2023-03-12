nx, ny, x, y, q = map(int, input().split())

items = {}
for _ in range(q):
    xi, yi = input().split()
    xy = (int(xi), int(yi))
    items.setdefault(xy, 0)
    items[xy] += 1

# ===
horse_steps = []
for i in (-1,+1):
    for j in (-2,+2):
        horse_steps.append((i,j))
        horse_steps.append((j,i))

import sys
from collections import deque
def solve(nx, ny, target_x, target_y, items):
    
    items = items.copy()

    dq = deque()
    dq.append((target_x, target_y))
    ret = 0
    
    xymap = [[None] * (ny+1) for _ in range(nx+1)]  # count from 1
    xymap[target_x][target_y] = 0
    if (target_x, target_y) in items:
        del items[(target_x, target_y)]  # because distance is 0

    while dq and items:
        x,y = dq.popleft()
        dist = xymap[x][y] + 1
        for dx, dy in horse_steps:
            qx = x+dx
            qy = y+dy
            # print(f"{x=}, {y=}, {qx=}, {qy=}", file=sys.stderr)
            if 1 <= qx <= nx and 1 <= qy <= ny:
                if xymap[qx][qy] is not None:
                    continue

                xymap[qx][qy] = dist
                qxy = (qx, qy)
                dq.append(qxy)
                if qxy in items:
                    ret += dist * items[qxy]
                    
                    del items[qxy]
        
    if items:  # some items left
        return None
    return ret


ret = solve(nx, ny, x, y, items)
if ret is None:
    print(-1)
else:
    print(ret)