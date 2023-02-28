import sys

n, m = input().split()  # n rows of m numbers
n, m = int(n), int(m)

lines = sys.stdin.readlines()
table = []

for line in lines:
    vals = list(map(int, line.split()))
    table.append(vals)

# assert max(map(len, table)) == min(map(len, table)), f"table"
# assert len(table) == n, f"{n=}"


def solve(table):
    dp = [[0] * (m) for _ in range(n)]
    dp[0][0] = table[0][0]

    # Init first row/col
    for i in range(1,m):
        dp[0][i] = table[0][i] + dp[0][i-1]

    for i in range(1,n):
        dp[i][0] = table[i][0] + dp[i-1][0]
    

    for col in range(1, m):
        for row in range(1, n):
            minprev = min(dp[row-1][col], dp[row][col-1])
            dp[row][col] = minprev + table[row][col]
    
    ret = dp[-1][-1] 
    # assert ret == dp[n-1][m-1], f"{n=}{m=}, {dp[-1][-1]} != {dp[n-1][m-1]}"

    print(dp, file=sys.stderr)
    return ret

ans = solve(table)

print(ans)