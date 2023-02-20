

import sys
lines = sys.stdin.readlines()

stack = []

for line in lines:
    cmd, *arg = line.split()
    
    if cmd == 'push':
        n = arg[0]
        stack.append(n)
        print('ok')

    elif cmd == 'pop':
        if stack:
            x = stack.pop()
            print(x)
        else:
            print('error')
        
    elif cmd == 'back':
        if stack:
            print(stack[-1])
        else:
            print('error')
    
    elif cmd == 'size':
        print(len(stack))

    elif cmd == 'clear':
        stack = []
        print('ok')

    elif cmd == 'exit':
        print('bye')
        break