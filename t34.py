import sys

nvert, nedg = map(int, input().split())

graph = {}
for line in sys.stdin.readlines():
    line = line.strip()
    if not line:  # skip empty line
        continue
    a,b = line.split()
    a = int(a); b = int(b)
    graph.setdefault(a, []).append(b)
    graph.setdefault(b, [])  # for max()


def solve(graph):
    """ Topological sorting """
    