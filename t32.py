import sys

n_vert, n_edges = map(int, input().split())

graph = {k: set() for k in range(1, n_vert+1)}  # maximal element
for line in sys.stdin.readlines():
    line = line.strip()
    if line:  # FIX: empty lines in tests
        a,b = line.split()
        a,b = int(a), int(b)
        graph[a].add(b)
        graph[b].add(a)


def solve(graph):
    if not graph:
        return []

    vertices = [None] * (len(graph) + 1)  # count from 1
    components = []

    iter_vertices = iter(vertices)
    next(iter_vertices)  # skip 0

    for iroot, val in enumerate(iter_vertices, 1):
        if val is not None:
            continue
        comp_idx = len(components)
        components.append([])

        stack = [iroot]
        while stack:
            s = stack.pop()
            if vertices[s] is not None:
                continue
            vertices[s] = comp_idx
            components[comp_idx].append(s)
            if s in graph:
                for ss in graph[s]:
                    if vertices[ss] is None:
                        stack.append(ss)
    
    return components

ans = list(solve(graph))
print(len(ans))
for xx in ans:
    print(len(xx))
    print(*sorted(xx))