import sys

n, m = input().split()
n, m = int(n), int(m)

lines = sys.stdin.readlines()
table = []

for line in lines:
    vals = list(map(int, line.split()))
    table.append(vals)

assert max(map(len, table)) == min(map(len, table)), f"table"
assert len(table) == n, f"{n=}"


def solve(table):
    dp = [[0] * m for _ in range(n)]

    