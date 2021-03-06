import sys
import itertools
#from random import randint

import timeit

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
	rev_deck = {}
	nums = None
	for line in sys.stdin:
		(letter,nums) = line.strip().split(':')
		nums = list(map(int, nums.split(',')))
		for n in nums:
			rev_deck[n]=letter
			
	# print (rev_deck)

	int_list = [v for v in rev_deck]
	#print(int_list)
	#QuickSort(int_list,0,len(int_list)-1)
	int_list = quickSort(int_list)
	#print(int_list)
	word = ''
	for q in int_list:
		word+=rev_deck[q]
	print (word)
	
start = timeit.default_timer()
main()
stop = timeit.default_timer()
print (stop-start)