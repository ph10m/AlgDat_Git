import sys
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

def binsearch(A,val):
	lo, hi, last = 0, len(A)-1, 0
	while lo<=hi:
		mid = (lo+hi)//2
		if val<A[mid]:
			hi = mid-1
		elif val>A[mid]:
			lo = mid+1
		else:
			return mid
	return mid

def find(A, _min, _max):
	lim = [0,0]
	a = binsearch(A,_min)
	lim[0] = A[a-1] if A[a]>_min and a!=0 else A[a]
	b = binsearch(A,_max)
	if b == len(A):
		b -= 1
	elif A[b]<_max and b<len(A)-1:
		b += 1
	lim[1] = A[b]
	return str(lim[0])+" "+str(lim[1])
	
	
def main():
	sorted = _quick([int(x) for x in sys.stdin.readline().split()])
	for line in sys.stdin:
		line = line.split()
		print(find(sorted, int(line[0]),int(line[1])))
		
main()