n = int(input())
vals = list(sorted(map(int, input().split())))
dist = [a-b for a,b in zip(vals[1:], vals[:-1])]


def solve(dist):
    acc_true  = dist[0]  # The first is always True
    acc_false = float('inf')  # fake branch to simplify the loop

    for i in range(1, len(dist)-1):
        # swap
        acc_false, acc_true = acc_true, acc_false

        # check new "True" candidate
        if acc_false < acc_true:  
            acc_true = acc_false  # drop the other branch
        acc_true += dist[i]  # "True" branch

    ret = min(acc_false, acc_true)
    
    if len(dist) > 1:
        ret += dist[-1]  # The last one is always True

    return ret

print(solve(dist))
