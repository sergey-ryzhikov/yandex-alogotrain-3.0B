n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

def solve(a, b):
    dp = [[0] * (len(b)+1) for _ in range(len(a) + 1)]  # count from 1
    
    for ia, xa in enumerate(a, 1):
        for ib, xb in enumerate(b, 1):
            nxt = max(dp[ia-1][ib], dp[ia][ib-1])  # left, top
            if xa == xb:
                nxt = dp[ia-1][ib-1] + 1  # diagonal
            dp[ia][ib] = nxt
    
    backpath = []

    # import sys
    # print(*dp, file=sys.stderr)

    while ia >= 1 and ib >= 1:
        
        xa = a[ia-1]
        xb = b[ib-1]

        # print(f"{ia=}, {ib=}, {xa=}, {xb=}", backpath, file=sys.stderr)
        if xa == xb:
            backpath.append(xa)
            ib -= 1
            ia -= 1
        elif dp[ia-1][ib] < dp[ia][ib-1]:
            ib -= 1
        else:
            ia -= 1
        
    return backpath

ans = reversed(solve(a,b))
print(*ans, end='')