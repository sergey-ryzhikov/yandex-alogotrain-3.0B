def prerr(*args):
    import sys
    print(*args,file=sys.stderr)

ops = set('*-+')

line = str(input())
tokens = line.split()
stack = []

for token in tokens:
    if token in ops:
        op = token
        assert len(stack) >= 2, 'Op for less then two operands'
        a, b = stack[-2:]  # pop last two elements
        del stack[-2:]
        try:
            if op == '*':
                a *= b
            elif op == '-':
                a -= b
            elif op == '+':
                a += b
            else:
                raise ValueError(f"Unhandled {op}")
        except TypeError:
            raise TypeError(f"wrong values '{a}' and '{b}' for operation '{op}'")
        
        stack.append(a)

    else:
        try:
            a = int(token)
        except ValueError:
            raise ValueError(f"Unknown token '{token}'")
        stack.append(a)
    
    # prerr(stack)

if len(stack) == 1:
    print(stack[0])
else:
    raise ValueError(f"Wrong input")