import sys

nrow, mcol = input().split()  # n rows of m numbers
nrow, mcol = int(nrow), int(mcol)

lines = sys.stdin.readlines()
table = []

for line in lines:
    vals = list(map(int, line.split()))
    table.append(vals)

# assert max(map(len, table)) == min(map(len, table)), f"table"
# assert len(table) == nrow, f"wrong len, {nrow=}"


# ----
def solve(table):
    dp = [[0] * (mcol) for _ in range(nrow)]
    dp[0][0] = table[0][0]

    # Init first row/col
    for i in range(1, mcol):
        dp[0][i] = table[0][i] + dp[0][i-1]

    for i in range(1, nrow):
        dp[i][0] = table[i][0] + dp[i-1][0]

    # Fill the table
    for c in range(1, mcol):
        for r in range(1, nrow):
            maxprev = max(dp[r-1][c], dp[r][c-1])
            dp[r][c] = maxprev + table[r][c]

    ans = dp[-1][-1]

    # print(*dp, sep="\n", file=sys.stderr)

    # find backpath
    backpath = []
    r = nrow-1; c = mcol-1
    while r > 0 or c > 0:
        cur = dp[r][c]
        up = dp[r-1][c] if r > 0 else 0
        left = dp[r][c-1] if c > 0 else 0

        # print(f"{cur=}, {up=}, {left=} {r=}, {c=}", file=sys.stderr)
        if up >= left and r > 0:
            r -= 1
            backpath.append('D')  # moved Down
        elif c > 0:
            c -= 1
            backpath.append('R')  # moved Right
        else:
            raise RuntimeError('niether R nor D')

    assert r==0 and c==0, "r or c not converged"
    return ans, backpath

maxsum, backpath = solve(table)

print(maxsum)
if backpath:
    print(*reversed(backpath))