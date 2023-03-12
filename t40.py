nstations = int(input())
nlines = int(input())

station_lines = {}  # station -> lines

for i in range(nlines):
    _, *stations = map(int, input().split())
    for st in stations:
        station_lines.setdefault(st, []).append(i)
    

start, end = map(int, input().split())

#===
from itertools import combinations
from collections import deque


def solve(station_lines, start, end):
    line_stations = {}
    for st, lines in station_lines.items():
        for line in lines:
            line_stations.setdefault(line, set()).add(st)

    connections = {}
    for l1,l2 in combinations(line_stations, 2):
        if line_stations[l1] & line_stations[l2]:  # common stations
            connections.setdefault(l1,[]).append(l2)
            connections.setdefault(l2,[]).append(l1)

    start_lines = set(station_lines[start])
    end_lines = set(station_lines[end])

    dq = deque()
    dq.extend(station_lines[start])

    scores = [None] * nlines
    for x in start_lines:
        scores[x] = 0

    if start_lines & end_lines:
        return 0

    while dq:
        l = dq.popleft()
        score = scores[l]
        if l not in connections:
            continue

        for lc in connections[l]:
            if scores[lc] is None:
                scores[lc] = score + 1
                dq.append(lc)
            elif scores[lc] < score:
                scores[lc] = score + 1

            if lc in end_lines:
                return scores[lc]

    return None

ans = solve(station_lines, start, end)

if ans is None:
    print(-1)
else:
    print(ans)