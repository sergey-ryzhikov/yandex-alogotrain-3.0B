
n = int(input())
train = list(map(int, input().split()))

assert n == len(train), f"Wrong {n=}"

stack = []
failed = False

itrain = iter(train)

for i in range(1, n+1):  # looking for i-th car
    # get car from stack
    if stack and i == stack[-1]:
        stack.pop()
        continue  # next i

    # get car from train
    for x in itrain:
        assert x >= i, f"Error: somehow skipped car '{x}'"
        if x == i:
            break  # move car from #1 to #2
        # put in stack
        stack.append(x)
    else: # not found i in train
        failed = True
        break
    
if stack or failed:
    print('NO')
else:
    print('YES')

    




        