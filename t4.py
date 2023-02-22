# import sys

n = int(input())
k = int(input())
row = int(input())
place = int(input())

assert n >= 2, f"err: {n=}"
assert 2 <= k <= n, f"err: {k=}"
assert row >= 1, f"err: {row=}"
assert place in (1,2), f"err: {place=}"
assert n >= (row-1) * 2 + place, f"err: {row=}, {place=}, {n=}"

def locate(row, place, k, n):
    """ 
        Output: (row, place); None
    """
    getrow = lambda i: i // 2 + 1
    getplace = lambda i: 2 if (i % 2) else 1  # 0->1, 1->2
    
    i = (row-1) * 2 + (place-1)   # petya pos, starting with 0
    x0 = i - k  # vasya pos candidate
    x1 = i + k  #
    r0, p0 = getrow(x0), getplace(x0)
    r1, p1 = getrow(x1), getplace(x1)
    
    x0_valid = True and x0 >= 0
    x1_valid = True and x1 < n 
    x0_better = True and abs(row-r0) < abs(row-r1)  # x1 is preferred on equal

    # print(f"{x0_valid=}, {x0_better=}, {x1_valid=}, {x0=}, {x1=}, {r1=}, {p1=}", file=sys.stderr)
    if x0_valid and (x0_better or not x1_valid):
        return r0, p0
    elif x1_valid and (not x0_better or not x0_valid):
        return r1, p1
    else:
        return None

ans = locate(row, place, k, n)
if ans is None: 
    print(-1)
else:
    print(*ans)