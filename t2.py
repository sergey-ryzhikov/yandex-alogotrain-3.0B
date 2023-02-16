import sys
def prerr(*args):
    print(*args,file=sys.stderr)

k = int(input()) 
text = str(input())

letters = set(text)

def get_score(text, letter, nrep=0):
    try:
        ileft = text.index(letter)
    except ValueError:
        raise ValueError(f"Letter '{letter}' not in text.")

    score = maxscore = 1  # at least one letter is present
    rep_used = 0

    for nxt in text[ileft:]:  # next letters
        if nxt == letter:
            score += 1
        else:
            if rep_used:
                # replace next character
                score += 1 
                rep_used -= 1
            else:
                # move left edge
                ileft += 1
                if text[ileft] == letter:
                    score -= 1
                else:
                    rep_used += 1

        if score > maxscore:
            maxscore = score
            
    return maxscore

# answer
print(max(get_score(text, letter, k) for letter in letters)) 



