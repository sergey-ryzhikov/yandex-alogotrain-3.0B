def prerr(*args):
    import sys
    print(*args,file=sys.stderr)

class Queue():
    def __init__(self, vals=[]):
        self.intems = []
        self.outems = list(vals)[:]  # copy
        self.outems.reverse()
        
    def put(self, val):
        self.intems.append(val)

    def get(self):
        if not self.outems:
            self.outems = self.intems
            self.intems = []
            self.outems.reverse()

        if not self.outems:
            raise IndexError("Getting from empty queue")

        return self.outems.pop()
    
    def __len__(self):
        return len(self.outems) + len(self.intems)

q1 = Queue(map(int, input().split()))
q2 = Queue(map(int, input().split()))

assert len(q1) == len(q2), \
                "Error: counts of items do not match"
assert len(q1) > 0, "Empty sequences"

winner = None

for i in range(0, 10**6):
    if len(q1) == 0:
        winner = 'second'
        break

    elif len(q2) == 0:
        winner = 'first'
        break
   
    a = q1.get()
    b = q2.get()
    
    if (a > b and not (a == 9 and b == 0)) or (a == 0 and b == 9):  # first wins
        q1.put(a)
        q1.put(b)
    else:  # second wins
        q2.put(a)
        q2.put(b)
        
    # prerr(a,b, 'lens:', len(q1), len(q2))

if winner is None:
    print('botva')
else:
    print(winner, i)