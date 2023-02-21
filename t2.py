
def prerr(*args):
    import sys
    print(*args,file=sys.stderr)

k = int(input()) 
text = str(input())

letters = 'abcdefghijklmnopqrstuvwxyz'
# assert len(set(letters)) == 26, "Error: letters"

def get_score(text, letter, nrep=0):

    score = maxscore = 0  # at least one letter is present
    rep_used = 0
    ileft = 0

    for nxt in text:
        if nxt == letter:
            score += 1
        else:
            # assert 0 <= rep_used <= nrep, f"err: {rep_used=}"
            if rep_used < nrep:
                # nxt replaced
                score += 1
                rep_used += 1
            else:
                # shrink
                while text[ileft] == letter:
                    ileft += 1
                    score -= 1
                ileft += 1

        if score > maxscore:
            maxscore = score

    return maxscore

# answer
print(max(get_score(text, letter, k) for letter in letters)) 