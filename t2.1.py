def prerr(*args):
    import sys
    print(*args,file=sys.stderr)

k = int(input()) 
text = str(input())

letters = 'abcdefghijklmnopqrstuvwxyz'
assert len(set(letters)) == 26, "Error: letters"


def max_beauty(text, nrepl=0):
    maxwidth = 0
    # stats = {a:[0,0] for a in letters}  # {letter: [replacements, width]}
    stats = [[a,0,0] for a in letters]

    for i,t in enumerate(text):
        for ic, (c, crepl, width) in enumerate(stats):
            if c == t:
                width += 1
            else:
                if crepl < nrepl:
                    crepl += 1
                    width += 1
                elif width == crepl:
                    continue
                else:
                    assert width <= i, f"err: {width=}, {i=}"
                    for j in range(i-width, i+1):
                        if text[j] != c:
                            break
                    width = i - j

            stats[ic][1:3] = crepl, width
            if maxwidth < width:
                maxwidth = width
    return maxwidth

print(max_beauty(text, k))
