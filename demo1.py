try:
    from itertools import pairwise   # Python 3.10

except ImportError:
    def pairwise(iterable):
        from itertools import tee
        # pairwise('ABCDEFG') --> AB BC CD DE EF FG
        a, b = tee(iterable)
        next(b, None)
        return zip(a, b)


n = int(input())
v = list(map(int, input().split()))

assert n == len(v), "Wrong n"

no_solution = False

for a,b in pairwise(v):
    if a > b:
        no_solution = True
        break

if no_solution:
    print(-1)
else:
    print(v[n-1] - v[0])   # max n steps

