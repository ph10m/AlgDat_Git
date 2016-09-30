import sys
# import math
def _quick(A):
	lo,pivs,hi = [],[],[]
	if len(A) <= 1: return A
	else:
		p = A[0]
		for i in A:
			if i < p: lo.append(i)
			elif i > p: hi.append(i)
			else: pivs.append(i)
		return _quick(lo) + pivs + _quick(hi)
	
from math import floor
def bsearch(A, v, p, r):
    if p > r:
        return p
    q = floor((p+r)/2)
    if A[q] >= v:
        return bsearch(A, v, p, q-1)
    else:
        return bsearch(A, v, q+1, r)

def binsearch(A,val):
	lo, hi, last = 0, len(A)-1, 0
	while lo<=hi:
		mid = floor((lo+hi)/2)
		last = mid
		if val<A[last]:
			hi = mid-1
		elif val>A[last]:
			lo = mid+1
		else:
			return last
	return last

def find(A, _min, _max):
	lim = [0,0]
	# a = bsearch(A,_min,0,len(A)-1)
	a = binsearch(A,_min)
	if A[a]>_min and a!=0:
		lim[0] = A[a-1]
	else:
		lim[0] = A[a]
	# b = bsearch(A,_max,0,len(A)-1)
	b = binsearch(A,_max)
	if b == len(A):
		b -= 1
	lim[1] = A[b]
	return str(lim[0])+" "+str(lim[1])
	
	
def main():
	_input = None
	_list = [int(x) for x in sys.stdin.readline().split()]
	# print(_list)
	sorted = _quick(_list)
	# print(sorted)
	for line in sys.stdin:
		line = line.split()
		# print ('Parsing line:',line)
		# print ('Reading: ',line)
		print(find(sorted, int(line[0]),int(line[1])))
		# print()
		#print(' '.join(str(x) for x in find(sorted,int(line[0]),int(line[1]))))

main()