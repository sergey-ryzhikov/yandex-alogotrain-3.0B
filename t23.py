n = int(input())

def calc(n):
    """ Operations: *2, *3, +1
    """
    seq = [n] * (n+1)  # whynot
    back = [None] * (n+1)  # backlog
    seq[1] = 0

    for i in range(1, n+1):
        s = seq[i]
        for x in (i*2, i*3, i+1):
            if x <= n and seq[x] >= s + 1:
                seq[x] = s + 1
                back[x] = i

    ret = seq[n]

    # backlog
    backlog = [n]
    x = n
    while back[x] is not None:
        backlog.append(back[x])
        x = back[x]

    return ret, list(reversed(backlog))

nop, oplog = calc(n)
print(nop)
print(*oplog)