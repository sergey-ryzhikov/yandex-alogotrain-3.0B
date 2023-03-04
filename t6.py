import sys

m = int(input())
n = int(input())

assert 1 <= m, f"err: {m=}"
assert 0 <= n, f"err: {n=}"

lines = sys.stdin.readlines()
assert len(lines) == n, f"err: {n=}, but {len(lines)} lines"

partitions = []  # we have at most 1000 partitions, so just put them in a list

for line in lines:
    a, b = line.split()
    a = int(a)
    b = int(b)
    assert a <= b, f"err: ({a=}) > ({b=})"
    partitions.append((a, b))


def partitions_overlap(partitions):
    """ Count overlapped partitions, inserted in a certain order.
        Return count.
    """
    arr = []  # (start, end) tuples
    for ax, bx in partitions:
        ileft, iright = 0, len(arr)  # 

        for i, (ai, bi) in enumerate(arr):
            if bx < ai:
                iright = i
                break
            elif ax > bi:
                ileft = i + 1
            else:  # overlap
                pass
        arr = arr[:ileft] + [(ax,bx)] + arr[iright:]
                    
    n_part = len(arr)
    return n_part


n_part = partitions_overlap(partitions)
print(n_part)
