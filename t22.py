import sys

n,k = input().split()
n = int(n); k=int(k)

def count_hog(n, k):
    #TODO: use deque
    log = [0,1,1]

    while len(log) <= n:
        if len(log) > k:
            nxt = log[-1] * 2 - log[-1-k]
        else:
            nxt = sum(log)
        log.append(nxt)
    
    # print(log, len(log), n, file=sys.stderr)
    return log[n]


print(count_hog(n,k))