nrow, mcol = input().split()  # n rows of m numbers
nrow, mcol = int(nrow), int(mcol)

def solve(nrow, mcol):
    if nrow < 3 or mcol < 3:
        if (nrow, mcol) in [(2,3), (3,2), (1,1)]:
            return 1
        return 0  # no solution

    dp = [[0] * mcol for _ in range(nrow)]  #FIXME: suboptimal
    dp[1][2] = dp[2][1] = 1

    for i in range(2, nrow):
        for j in range(2, mcol):
            dp[i][j] = dp[i-1][j-2] + dp[i-2][j-1]

    ret = dp[nrow-1][mcol-1]
    return ret


ans = solve(nrow, mcol)
print(ans)