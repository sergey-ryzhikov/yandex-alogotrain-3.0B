n = int(input())
vals = list(sorted(map(int, input().split())))
dist = [None, None] + [a-b for a,b in zip(vals[1:], vals[:-1])]

def solve(dist):
    dp = [None] * (len(dist))
    dp[0] = dp[1] = dp[2] = dist[2]
    
    for i in range(3, len(dist)):
        assert i>=2, f"{i=} <2"
        dp[i] = min(dp[i-2], dp[i-1]) + dist[i]

    ret = dp[-1]
    return ret

print(solve(dist))