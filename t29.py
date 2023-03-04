import sys

n = int(input())  # N
prices = list(map(int, sys.stdin.readlines()))
assert n == len(prices), "N"

def solve(prices):
    if not prices:
        return 0, 0, []

    dp = []
    hist = []

    #  base
    if prices[0] > 100:
        dp.append([float('inf'), prices[0]])  # one coupon since the beginning
    else:
        dp.append([prices[0]])
    
    hist.append([0, 1])  # works both for 0 or 1 coupons on step 0

    for i in range(1, len(prices)):
        price = prices[i]
        prev = dp[-1]

        if price > 100:
            # obtain coupons
            cur =  [float('inf')] + [p + price for p in prev]
            hcur = [None] + [x-1 for x in range(1, len(cur))]
        else:
            # do not obtain coupons
            cur = [p + price for p in prev]
            hcur = [x for x in range(len(cur))]

        # spend previous coupons
        for j, p in enumerate(prev[1:]):
            if cur[j] > p:
                cur[j] = p
                hcur[j] = j + 1

        dp.append(cur)
        hist.append(hcur)

    assert len(dp) == len(prices), "Length mismatch"

    rindex = lambda l, x: len(l) - list(reversed(l)).index(x) - 1

    summ = min(dp[-1])
    ncoupons = rindex(dp[-1], summ)  # number of coupons left

    # get back path
    backdays = []
    # 
    j_next = ncoupons
    for i, h in reversed(list(enumerate(hist))):
        # print(f"{hist=}, {j_next=}", file=sys.stderr)
        j = h[j_next]
        if j > j_next:  # coupons spent
            backdays.append(i+1)  # count from 1
        j_next = j

    days = list(reversed(backdays))
    return summ, ncoupons, days


summ, ncoupons, days = solve(prices)
print(summ, )
print(ncoupons, len(days))
print(*days, sep='\n', end='')