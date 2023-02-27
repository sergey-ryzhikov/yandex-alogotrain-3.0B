n = int(input())
vals = list(sorted(map(int, input().split())))

dist = [a-b for a,b in zip(vals[1:], vals[:-1])]


def mindist(dist):
    assert len(dist) >= 2, f"{len(dist)=}"

    def func(i=1, prev=(False, True)):
        if i >= len(dist) - 1:
            return 0  # End

        score_false = score_true = float('inf')

        # False
        if prev[1] != False:
            score_false = func(i+1, (prev[1], False))
        # True
        if prev != (True, True):
            score_true = func(i+1, (prev[1], True))
            score_true += dist[i]
        
        return min(score_false, score_true)

    acc = dist[0] + dist[-1]  # First and last are always True
    acc += func()
    return acc

print(mindist(dist))
