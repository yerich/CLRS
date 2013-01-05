import random
import time
def countingSort(A, k):
    k += 1
    B = []
    C = []
    for i in range(0, k):
        C.append(0)
    
    for i in A:
        B.append(0)
        C[i] += 1
    
    i=1
    while(i < len(C)):
        C[i] += C[i-1]
        i += 1
    
    i=0
    while(i < len(A)):
        B[C[A[i]]-1] = A[i]
        C[A[i]] -= 1
        i += 1
    
    i=0
    while(i < len(A)):
        A[i] = B[i]
        i += 1

array = [1, 5, 4, 3, 2, 6, 7, 12, 8, 11, 9, 10]
countingSort(array, 12)
print array

array = [random.randint(0,10) for x in xrange(1000000)]
print "Beginning large sort..."
start = time.time()
countingSort(array, 10)
print "Done. It took", round(time.time() - start, 4), "seconds."