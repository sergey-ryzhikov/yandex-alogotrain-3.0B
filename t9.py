nrows, ncols, nreq = map(int, input().split())

matrix = []
for _ in range(nrows):
    vals = list(map(int, input().split()))
    matrix.append(vals)

assert nrows == len(matrix), "nrows"

requests = []
for _ in range(nreq):
    x1, y1, x2, y2 = map(int, input().split())
    requests.append((x1,y1,x2,y2))

# ===
from itertools import accumulate
import sys

def cumsum(matrix):
    if not matrix:
        return [0]
    rows = len(matrix)
    cols = len(matrix[0])

    ret = [[0] * (cols + 1)]# count from 1

    for i,row in enumerate(matrix):
        cs_row = [0] + list(accumulate(row))
        ret.append([a+b for a,b in zip(ret[i], cs_row)])
    
    return ret

cs = cumsum(matrix)
# print(*cs, sep='\n', file=sys.stderr)
# print(*requests, sep='\n', file=sys.stderr)

def solve(cs, x1,y1,x2,y2):
    x0, y0 = x1-1, y1-1
    return cs[x2][y2] - cs[x0][y2] - cs[x2][y0] + cs[x0][y0]

ans = (solve(cs, *x) for x in requests)
print(*ans, sep='\n')