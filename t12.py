
chars = str(input())

stack = []

brackets = {'(':')', '[':']', '{':'}'}
brackets_inv = dict((v,k) for k,v in brackets.items())

err = False

for char in chars:
    if char in brackets:
        stack.append(char)
    elif char in brackets_inv:
        char_inv = brackets_inv[char]
        if not stack:  # a closing bracket without any open ones
            err = True
            break
        if stack[-1] == char_inv:  # match
            stack.pop()
        else:
            err = True
            break
    else:
        raise ValueError(f"Unknown symbol {char}")

if err or stack:  # not empty
    print('no')
else:
    print('yes')


