
n = int(input())
vals = list(map(int, input().split()))
k = int(input())
targs = list(map(int, input().split()))

assert len(vals) == n, "wrong length (vals)"
assert len(targs) == k, "wrong length (targs)"

svals = list(sorted(set(vals)))

def binsearch_less(slist, item):
    """ Returns leftmost item index in sorted list
        which is smaller then item
        or None.
    """

    if not len(slist):
        return None

    left, right = 0, len(slist)  # [left, right)
    prev_mid = 0

    while left != right:
        mid = (left + right) // 2
        if mid == prev_mid:
            break

        if slist[mid] >= item:
            right = mid
        else:
            left = mid

        # print(f"{left=}, {right=}, {mid=}: {slist[mid]} : {slist=}, {item=}")
        prev_mid = mid

    if slist[left] >= item:
        return None
    else:
        return left

# func = binsearch_less
# print(func([1], 2), 0)
# print(func([1,2,3], 2), 0)
# print(func([1,2,3,4,5], 6), 4)
# print(func([1,2,3,4,5], 0), None)
# print(func([1,2,3,4,5], 1), None)
# print(func([1,2,3,4,5], 2), 0)
# print(func([1,2,4,5,6], 3), 1)

for targ in targs:
    itop = binsearch_less(svals, targ)

    if itop is not None:
        cnt = 1 + itop  # index in list is a number of smaller values
    else:
        cnt = 0

    print(cnt)
    
