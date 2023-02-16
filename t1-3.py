
n = int(input())
vals = list(map(int, input().split()))
k = int(input())
targs = list(map(int, input().split()))

assert len(vals) == n, "wrong length (vals)"
assert len(targs) == k, "wrong length (targs)"

svals = list(sorted(set(vals)))

# def binsearch(slist, item):
#     """ Returns item index or None """
#     low = 0
#     high = len(slist) - 1

#     if high == -1:  # empty slist
#         return None

#     while high != low:
#         mid = (low + high) // 2

#         if slist[mid] < item:  # right
#             low = mid 
#         else:  # left
#             high = mid
        
#         print(low, high)

#     if slist[low] != item:
#         return None
#     else:
#         return low

# print(binsearch([1], 1))
# print(binsearch([1,2,3], 2))
# # print(binsearch([1,2,3,4,5], 6))
# # print(binsearch([1,2,3,4,5], 0))
# # print(binsearch([1,2,3,4,5], 3))

for targ in targs:
    itop = None

    for i,v in enumerate(svals):
        if v >= targ:
            break
        else:
            itop = i

    if itop is not None:
        cnt = 1 + itop  # index in list is a number of smaller values
    else:
        cnt = 0
    print(cnt)
    
