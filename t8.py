_ = int(input())

import sys

ans = None

def update(ans,x,y):
    if ans is None:
        return x,y,x,y

    x1,y1,x2,y2 = ans

    x1 = min(x1,x)
    x2 = max(x2,x)
    y1 = min(y1,y)
    y2 = max(y2,y)

    return x1,y1,x2,y2

for line in sys.stdin.readlines():
    x,y = map(int, line.split())
    ans = update(ans, x,y)

print(*ans)