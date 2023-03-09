import sys

n = int(input())
arr = [[] * n for _ in range(n)]

graph = {x:set() for x in range(1,n+1)}
for i,line in enumerate(sys.stdin.readlines(), start=1):
    vals = line.split()
    assert len(vals) == n, f"err: line #{i}"
    for j,val in enumerate(vals, start=1):
        if val == '1':
            graph[i].add(j)


def solve(graph):
    """ find any cycle """
    if not graph:
        return None

    visited = [None] * (max(graph.keys()) + 1)  # None, 1, 2
    ret = []

    for k in graph:
        if visited[k] is not None:
            continue
        # start for k
        stack = [k]

        while stack:
            # print(stack, file=sys.stderr)
            s = stack.pop()
            if visited[s] is None:
                visited[s] = 1
            for c in graph[s]:
                vc = visited[c]

                if vc is None:
                    # go deeper
                    visited[c] = 1
                    stack.append(s)
                    stack.append(c)
                    break
                elif vc == 1:
                    if not stack or stack[-1] == c:  # child is the parent at the same time
                        pass
                    else:
                        # Cycle found
                        ret = stack[stack.index(c):] + [s]
                        stack = []
                        break
                elif vc == 2:
                    pass
                else:
                    raise ValueError(f"impossible {vc=}")
            else:
                # Done with s
                visited[s] = 2

        if ret:
            return ret
        else:
            continue  # next k

# print(graph, file=sys.stderr)
ans = solve(graph)
if ans is None:
    print('NO')
else:
    print('YES')
    print(len(ans))
    print(*reversed(ans))

