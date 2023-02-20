class MaxHeap:
    def __init__(self):
        self.arr = []

    def insert(self, k):
        arr = self.arr
        pos = len(arr)  # last element + 1
        arr.append(k)

        # sift-up
        while pos > 0:
            parent_pos = (pos - 1) // 2
            if arr[parent_pos] < k:  # swap
                arr[parent_pos], arr[pos] = k, arr[parent_pos]
                pos = parent_pos
            else:
                break
        
    def extract(self):
        arr = self.arr

        if not arr:  # empty heap
            raise IndexError("Extracting from empty heap.")

        if len(arr) == 1:  # return single element
            return arr.pop()
        
        n = len(arr) - 1  # new length
        ret = arr[0]
        arr[0] = last = arr[-1]  # move last to first, then sift-down
        
        pos, child_pos = 0, 1
        while child_pos < n:
            # select left or right child
            if arr[child_pos] < arr[child_pos+1]:
                child_pos += 1  # select right child
            if arr[child_pos] > arr[pos]:  # swap
                arr[child_pos], arr[pos] = arr[pos], arr[child_pos]
                pos = child_pos
            else:
                break
            child_pos = pos * 2 + 1
        del arr[-1]  # always delete the last one
        return ret
# ===

import sys
n = int(input())
lines = sys.stdin.readlines()

assert len(lines) == n, f"Wrong number of lines {n=}"

heap = MaxHeap()

for line in lines:
    cmd, *args = line.split()
    cmd = int(cmd)
    if args:
        args = list(map(int, args))
    
    if cmd == 0:  # insert
        heap.insert(args[0])
    elif cmd == 1:
        x = heap.extract()
        print(x)
    else:
        raise ValueError(f"Unknown {cmd=}")
