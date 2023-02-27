import sys
n = int(input())

times = []
for line in sys.stdin.readlines():
    a,b,c = map(int,line.split())
    times.append((a,b,c))


def mintime(times):
    n = len(times)
    k = 3

    dp = [[] for _ in range(n+k)]
    dp[0] = [0]

    for i, abc in enumerate(times):
        prev = min(dp[i])
        a,b,c = (prev + x for x in abc)
        dp[i+1].append(a)
        dp[i+2].append(b)
        dp[i+3].append(c)
        # print(dp)
    
    return min(dp[n])

print(mintime(times))