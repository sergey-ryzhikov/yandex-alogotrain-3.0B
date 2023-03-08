import sys

nvert, nedg = map(int, input().split())

graph = {}
for line in sys.stdin.readlines():
    line = line.strip()
    if not line:
        continue
    a,b = line.split()
    a = int(a); b = int(b)
    if a == b:
        raise ValueError(f'{a=}, {b=}')
    graph.setdefault(a, []).append(b)
    graph.setdefault(b, [])


def solve(graph):
    """ Check can paint in two colors.
    """
    if not graph:
        return True
        
    colors = [None] * (max(graph) + 1)  # None - no, 1, 2
    next_color = lambda c: 3 - c

    for k in graph:
        if colors[k] is not None:
            continue
        # start with k
        stack = [k]
        colors[k] = 1
        while stack:
            s = stack.pop()
            children = graph[s]
            parent_color = colors[s]
            child_color = next_color(parent_color)
            for child in children:
                cc = colors[child]  # actual child color
                if cc == child_color:
                    continue
                elif cc == parent_color:
                    return False  #
                elif cc is None:
                    stack.append(s)
                    stack.append(child)
                    colors[child] = child_color
                    break  # go deeper   
                else:
                    raise ValueError(f"Impossible value {cc=}")

    # print(f"{colors=}", file=sys.stderr)
    return True

print(graph, file=sys.stderr)

ans = solve(graph)
print('YES' if ans else 'NO')