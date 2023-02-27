n = int(input())
vals = list(map(int, input()))

dist = [a-b for a,b in zip(vals[1:], vals[:-1])]




print(func(dist))
