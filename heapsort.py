import random
from math import floor
import time

def swap(A, x, y):
    tmp = A[x]
    A[x] = A[y]
    A[y] = tmp

class Heap:
    def __getitem__(self, key):
        return self.data[key]
    
    def __setitem__(self, key, value):
        self.data[key] = value
    
    def __len__(self):
        return len(self.data)
    
    data = []
    heap_size = 0

def left(p):
    return 2*p

def right(p):
    return 2*p + 1

def parent(p):
    return floor(p/2)

def maxHeapify(A, i):
    l = left(i)
    r = right(i)
    if(l < A.heap_size and A[l] > A[i]):
        largest = l
    else:
        largest = i
    
    if(r < A.heap_size and A[r] > A[largest]):
        largest = r
    
    if(largest != i):
        swap(A, i, largest)
        maxHeapify(A, largest)

def buildMaxHeap(A):
    A.heap_size = len(A)
    i = int(floor(len(A) / 2))
    while i >= 0:
        maxHeapify(A, i)
        i -= 1

def heapsort(A):
    buildMaxHeap(A)
    i = len(A)-1
    while i >= 1:
        swap(A, 0, i)
        A.heap_size -= 1
        maxHeapify(A, 0)
        i -= 1

if __name__ == "__main__":
    A = Heap()
    A.data = [1, 5, 4, 3, 2, 6, 7, 12, 8, 11, 9, 10]
    heapsort(A)
    print A.data
    
    A.data = random.sample(range(1000000), 1000000)
    print "Beginning large sort..."
    start = time.time()
    heapsort(A)
    print "Done. It took", round(time.time() - start, 4), "seconds."