
def prerr(*args):
    import sys
    print(*args,file=sys.stderr)

k = int(input()) 
text = str(input())

letters = 'abcdefghijklmnopqrstuvwxyz'
assert len(set(letters)) == 26, "Error: letters"

def get_score(text, letter, nrep=0):
    try:
        start = max(0, text.index(letter) - nrep)  # earliest possible replacement
    except ValueError:
        #raise ValueError(f"Letter '{letter}' not in text.")
        return 0

    score = maxscore = 0  # at least one letter is present
    rep_used = 0

    ileft = start  # the first letter

    for i in range(start, len(text)):
        nxt = text[i]
        
        if nxt == letter:
            score += 1
        elif rep_used < nrep:  # can replace
            rep_used += 1
            score += 1
        else:  # have to move ileft (shrink the sequence)
            if not rep_used:  # no replacements were made
                ileft = i
                score = 0
            else:
                # Find the earliest replacement
                for ileft in range(ileft, i):  # up to previous element
                    if text[ileft] == letter:
                        score -= 1
                        assert score >= 0, f"Negative score? {score=}"
                    else:  # found one
                        ileft += 1
                        break

        if score > maxscore:
            maxscore = score

        # prerr(f"{letter=}, {nxt=}, {ileft=}, {rep_used=}, {score=}, {maxscore=}")
        
    return maxscore

# answer
print(max(get_score(text, letter, k) for letter in letters)) 



