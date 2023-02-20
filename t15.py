
n = int(input())
vals = list(map(int, str(input()).split()))

assert len(vals) == n, f"Wrong {n=}"

stack = []  # (pos, val)
ans = [-1] * n

for pos, val in enumerate(vals):

    while stack:
        spos, sval = stack[-1]
        if sval > val:  # found it's place
            ans[spos] = pos
            stack.pop()
            continue
        else:
            break

    stack.append((pos, val))

print(*ans, sep=' ')