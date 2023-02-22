import sys

m = int(input())
n = int(input())

assert 1 <= m, f"err: {m=}"
assert 0 <= n, f"err: {n=}"

lines = sys.stdin.readlines()
assert len(lines) == n, f"err: {n=}, but {len(lines)} lines"

partitions = []  # we have at most 1000 partitions, so just put them in a list

for line in lines:
    a, b = lines.split()
    a = int(a); b = int(b)
    assert a <= b, f"err: ({a=}) > ({b=})"
    partitions.append(tuple(a,b))

def partitions_overlap(partitions):
    """ Count overlapped partitions, inserted in a certain order.
        Return count.
    """
    

    for start, end in partitions:
        

    
    assert len(scheme) % 2 == 0, "err: scheme length is not even"

    n_part = len(scheme) / 2
    return n_part

n_part = partitions_overlap(partitions)
print(len(n_part))

