import random
import time

def merge(L, p, q, r):
	n = q - p + 1
	m = r - q
	
	A = []
	B = []
	
	for i in range(p, q+1):
		A.append(L[i])
	for i in range(q+1, r+1):
		B.append(L[i])
	
	i = 0
	cA = 0
	cB = 0
	while(i < n+m):
		if(cA < len(A) and (cB >= len(B) or A[cA] <= B[cB])):
			L[p+i] = A[cA]
			cA += 1
		else:
			L[p+i] = B[cB]
			cB += 1
		i += 1

def mergesort(L, a, b):
	if(b <= a): 
		return
	n = int((b+a)/2)
	mergesort(L, a, n)
	mergesort(L, n+1, b)
	merge(L, a, n, b)

array = [1, 5, 4, 3, 2, 6, 7, 12, 8, 11, 9, 10]
mergesort(array, 0, 11)
print array

array = random.sample(range(1000000), 1000000)
print "Beginning large sort..."
start = time.time()
mergesort(array, 0, len(array)-1)
print "Done. It took", round(time.time() - start, 4), "seconds."