import sys
n = int(input())
lines = sys.stdin.readlines()

assert 1 <= n <= 26, f"err: {n=}"
assert n == len(lines), f"err: {n=} for {len(lines)} lines"

vals = list(map(int, lines))

def pairwise(vals):
    a = iter(vals)
    b = iter(vals)
    next(b, None)
    return zip(a,b)

def goodness(vals):
    ret = 0
    for x,y in pairwise(vals):
        ret += min(x,y)
    return ret

ans = goodness(vals)
print(ans)