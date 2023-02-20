import operator

class Heap:
    def __init__(self, op=operator.lt): 
        self.arr = []
        self.op = op

    def insert(self, k):
        arr = self.arr
        pos = len(arr)  # last element + 1
        arr.append(k)

        # sift-up
        while pos > 0:
            parent_pos = (pos - 1) // 2
            if self.op(k, arr[parent_pos]):  # swap
                arr[parent_pos], arr[pos] = k, arr[parent_pos]
                pos = parent_pos
            else:
                break

    def extract(self):
        arr = self.arr
        op = self.op

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
            if op(arr[child_pos+1], arr[child_pos]):
                child_pos += 1  # select right child
            if op(arr[child_pos], arr[pos]):  # swap
                arr[child_pos], arr[pos] = arr[pos], arr[child_pos]
                pos = child_pos
            else:
                break
            child_pos = pos * 2 + 1
        del arr[-1]  # always delete the last one
        return ret

    def __len__(self):
        return(len(self.arr))

    def __iter__(self):
        return self

    def __next__(self):
        try:
            val = self.extract()
        except IndexError:
            raise StopIteration
        return val


class MinHeap(Heap):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs, op=operator.lt)

class MaxHeap(Heap):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs, op=operator.gt)
    
# ===

n = int(input())
inumbers = map(int, input().split())

heap = MinHeap()

for num in inumbers:
    heap.insert(num)

print(*heap)