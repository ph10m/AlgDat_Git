import sys
from random import randint
import math

def QuickSort(A,start,end):
    if start<end:
        pivot=randint(start,end)
        temp=A[end]
        A[end]=A[pivot]
        A[pivot]=temp
        
        p=Partition(A,start,end)
        QuickSort(A,start,p-1)
        QuickSort(A,p+1,end)


def Partition(A,start,end):
    pivot=randint(start,end)
	#swap
    temp=A[end]
    A[end]=A[pivot]
    A[pivot]=temp
    pivot_ind=start-1
    for index in range(start,end):
        if A[index]<A[end]:#check if current val is less than pivot value
            pivot_ind=pivot_ind+1
            temp=A[pivot_ind]
            A[pivot_ind]=A[index]
            A[index]=temp
    temp=A[pivot_ind+1]
    A[pivot_ind+1]=A[end]
    A[end]=temp
    return pivot_ind+1
	
def binSearch(A,p,r,v):
	i=p
	if p<r:
		q=math.floor((p+r)/2)
		if v <= A[q]:
			i=binSearch(A,p,q,v)
		else:
			i = binSearch(A,q+1,r,v)
	return i
	
def find(A,_min,_max):
	ind_min = binSearch(A,0,len(A)-1,_min)
	ind_max = binSearch(A,0,len(A)-1,_max)
	return [A[ind_min],A[ind_max]]
			

def main():
	_input = []
	for x in sys.stdin.readline().split():
		_input.append(int(x))
	
	QuickSort(_input,0,len(_input)-1)
	#print (_input)
	
	for indexes in sys.stdin:
		word = indexes.split()
		_min = int(word[0])
		_max = int(word[1])
		#print (word)
		#find(_input, _min, _max)
		result = find(_input, _min, _max)
		print(str(result[0]) + " " + str(result[1]))

main()