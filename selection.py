import random
import time

def partition(A, i, k):
	j = i
	
	while i < k:
		if(A[i] < A[k]):
			tmp = A[i]
			A[i] = A[j]
			A[j] = tmp
			j += 1
		
		i += 1
	
	tmp = A[j]
	A[j] = A[k]
	A[k] = tmp
	
	return j

def select_lowest_from_list(A, i, j, k):
	if(j-i < 1):
		return A[i]
	
	p = partition(A, i, j)
	if(p == i + k - 1):
		return A[p]
	elif(p > i + k - 1):
		return select_lowest_from_list(A, i, p-1, k)
	else:
		return select_lowest_from_list(A, p+1, j, k-(p-i+1))

array = [3,2,6,5,7,1,8]
print partition(array, 0, 6)
print select_lowest_from_list(array, 0, 6, 7)
print array

array = random.sample(range(1000000), 1000000)
print "Beginning large sort..."
start = time.time()
print select_lowest_from_list(array, 0, len(array)-1, 500000)
print "Done. It took", round(time.time() - start, 4), "seconds."