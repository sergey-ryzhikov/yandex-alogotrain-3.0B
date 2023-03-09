import sys

nvert, nedg = map(int, input().split())

graph = {x:[] for x in range(1, nvert+1)}
for line in sys.stdin.readlines():
    line = line.strip()
    if not line:  # skip empty line
        continue
    a,b = line.split()
    a = int(a); b = int(b)
    graph.setdefault(a, []).append(b)
    graph.setdefault(b, [])


def solve(graph):
    """ Topological sorting + loop detection. """
    if not graph:
        return []
    
    visited = [None] * (max(graph.keys()) + 1)  # None, 1, 2
    ret = []

    for k in graph:
        if visited[k] is not None:
            continue
        stack = [k]
        while stack:
            s = stack.pop()
            if visited[s] is None:
                visited[s] = 1

            for child in graph[s]:
                vc = visited[child]

                if vc is None:
                    stack.append(s)
                    stack.append(child)
                    visited[child] = 1
                    break
                elif vc == 1:  # already in path
                    # if s == child:  # loop
                    #     pass
                    # else:
                    #     # Cycle found
                        return None
                elif vc == 2:
                    pass
                else:
                    raise ValueError(f"{vc=}")
            else:
                # finished or no children
                ret.append(s)
                visited[s] = 2
            # print(f"{stack=}", file=sys.stderr)
    return ret

# print(f"{graph=}", file=sys.stderr)
ans = solve(graph)
if ans is None:
    ans = [-1]
print(*reversed(ans))