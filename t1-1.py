import sys

lines = sys.stdin.readlines()

counts = {}
ignore_chars = ' \n'

for line in lines:
    for char in line:
        counts[char] = counts.get(char, 0) + 1

for char in ignore_chars:
    if char in counts:
        del counts[char]

def print_hist(counts):
    keys = list(sorted(counts.keys()))
    vals = [counts[k] for k in keys]

    # print bins
    maxbin = max(counts.values())
    for i in reversed(range(1,maxbin+1)):
        row = ''.join('#' if v >= i else ' ' for v in vals)
        print(row)

    # print labels
    print(''.join(keys))

print_hist(counts)