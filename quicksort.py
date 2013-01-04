import random
import time

def swap(A, x, y):
    tmp = A[x]
    A[x] = A[y]
    A[y] = tmp

def partition(A, p, r):
    x = A[r]
    i = p-1
    
    j = p
    while j < r:
        if(A[j] <= x):
            i += 1
            swap(A, i, j)
        j += 1
    
    swap(A, i+1, r)
    return i+1

def randomizedPartition(A, p, r):
    swap(A, r, random.randint(p, r))
    return partition(A, p, r)

def quicksort(A, p, r):
    if(p < r):
        q = partition(A, p, r)
        quicksort(A, p, q-1)
        quicksort(A, q+1, r)

def randomizedQuicksort(A, p, r):
    if(p < r):
        q = randomizedPartition(A, p, r)
        randomizedQuicksort(A, p, q-1)
        randomizedQuicksort(A, q+1, r)

array = [1, 5, 4, 3, 2, 6, 7, 12, 8, 11, 9, 10]
quicksort(array, 0, len(array)-1)
print array
array = [1, 5, 4, 3, 2, 6, 7, 12, 8, 11, 9, 10]
randomizedQuicksort(array, 0, len(array)-1)
print array

array = random.sample(range(1000000), 1000000)
print "Beginning large sort..."
start = time.time()
randomizedQuicksort(array, 0, len(array)-1)
print "Done. It took", round(time.time() - start, 4), "seconds."