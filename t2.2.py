def prerr(*args):
    import sys
    print(*args,file=sys.stderr)

# k = int(input()) 
text = str(input())

letters = 'abcdefghijklmnopqrstuvwxyz'
assert len(set(letters)) == 26, "Error: letters"


def compress(text):
    """ Compress text into list of tuples for each letter.
        Example:  abbaaa -> {a: [(1,2),(3,0)], b: [(1,2),(0,3)]}
    """
    char_counts = {}

    ret = {}  # {letter: [(count_char, count_nonchar), ...], ...}

    for i,t in enumerate(text):
        char_counts.setdefault(t, [0,i])  # [char, non_char]
        for char, counts in char_counts.items():
            if char != t:
                counts[1] += 1
            else:
                if counts[1] == 0:  # previos was not non_char
                    counts[0] += 1
                else:
                    ret.setdefault(char, [])
                    ret[char].append(tuple(counts))
                    counts[:] = 1,0
    else:
        for char, counts in char_counts.items():
            ret.setdefault(char, [])
            ret[char].append(tuple(counts))
    return ret

print(compress(text))