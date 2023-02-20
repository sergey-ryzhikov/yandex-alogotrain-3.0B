from collections import deque
import sys

lines = sys.stdin.readlines()

q = deque()

for line in lines:
    cmd, *args = line.split()

    if cmd == 'push_front':
        n = int(args[0])
        q.append(n)
        print('ok')

    if cmd == 'push_back':
        n = int(args[0])
        q.appendleft(n)
        print('ok')

    elif cmd == 'pop_front':
        try:
            item = q.pop()
        except IndexError:
            print('error')
        else:
            print(item)

    elif cmd == 'pop_back':
        try:
            item = q.popleft()
        except IndexError:
            print('error')
        else:
            print(item)

    elif cmd == 'front':
        try:
            item = q[-1]
        except IndexError:
            print('error')
        else:
            print(item)

    elif cmd == 'back':
        try:
            item = q[0]
        except IndexError:
            print('error')
        else:
            print(item)

    elif cmd == 'size':
        print(len(q))

    elif cmd == 'clear':
        q.clear()
        print('ok')

    elif cmd == 'exit':
        print('bye')
        break
