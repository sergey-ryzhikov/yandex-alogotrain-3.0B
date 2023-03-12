import sys

line = sys.stdin.readline().strip()

seq = lambda n,i: n + i * (n - i - 1)   # magic

# for i in range(3,10):
#     print([seq(i,x) for x in range(i)])

def solve(line):
    n = len(line)
    cnt = {}
    for i,char in enumerate(line):
        cnt.setdefault(char, 0)
        cnt[char] += seq(n, i)
    return cnt

ans = solve(line)
for ch in sorted(ans):
    print(f"{ch}: {ans[ch]}")