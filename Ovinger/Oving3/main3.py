import sys
import math
# import itertools
#from random import randint

import timeit
def merge(A):
	half = None
	output = []
	_size = len(A)
	if len(A)%2==0:
		half = len(A)/2
	else:
		half = (len(A)+1)/2
	left = A[:half]
	right = A[half:]
	left.append(1000001)
	right.append(1000001)
	#print ("Left: ",left)
	#print("Right: ",right)
	#print(left[0][1])
	i,j=0,0
	while len(output)<_size:
		_l,_r = left[i][1], right[j][1]
		if _l==1:
			#left is smaller:
			output.append(left[i])
			i+=1
		else:
			output.append(right[j])
			j+=1
		#print ('Output[] = ',output)
	
	return None

def quickSort(arr):
    less = []
    pivotList = []
    more = []
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        for i in arr:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotList.append(i)
        less = quickSort(less)
        more = quickSort(more)
        return less + pivotList + more

def main():
	deck = []
	nums = None
	for line in sys.stdin:
		(letter,nums) = line.strip().split(':')
		nums = list(map(int, nums.split(',')))
		for n in nums:
			deck.append((letter,n))
			
	#print(deck)
	print(merge(deck))
	
start = timeit.default_timer()
main()
stop = timeit.default_timer()
print (stop-start)