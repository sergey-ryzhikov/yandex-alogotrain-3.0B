import sys

nvert, nedg = map(int, input().split())


graph = {}
for line in sys.stdin.readlines():
    line = line.strip()
    if not line:
        continue
    a,b = line.split()
    a = int(a); b = int(b)
    graph.setdefault(a, set()).add(b)
    graph.setdefault(b, set())



def solve(graph):
    """ Check all components are bipartite with no cycles
    """
    visited = [None] * (len(graph) + 1)  # None - no, 1 - visited, 2 - done
    # for k in graph:
    #     if visited[k] is None:
    #         # DFS from k
    #         stack = [k]
    #         visited[k] = 1
    #         while stack:
    #             s = stack.pop()
    #             children_undone = [c for c in graph[s] if visited[c] != 2]
    #             for c in children_undone:
    #                 if visited[c] == 1:  # cycle found
    #                     return False
    #                 elif visited[c] is None:
    #                     stack.append(s)
    #                     stack.append(c)
    #                     visited[c] = 1
    #                     break
    #             else:
    #                 visited[s] = 2  # done

    #             print(f"{visited=}", file=sys.stderr)
    return True

print(graph, file=sys.stderr)

ans = solve(graph)
print('YES' if ans else 'NO')