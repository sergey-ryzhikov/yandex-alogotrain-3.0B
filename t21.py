n = int(input())

def count_no_111(n):
    first = {0:0, 1:2, 2:4, 3:7, 4:13}
    if n <= 4:
        return first[n]
    else:
        return count_no_111(n-1) * 2 - count_no_111(n-4)

print(count_no_111(n))