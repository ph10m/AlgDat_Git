import sys
import itertools
#from random import randint

import timeit

def partition(array, begin, end):
    pivot = begin
    for i in range(begin+1, end+1):
        if array[i] <= array[begin]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[begin] = array[begin], array[pivot]
    return pivot


def quicksort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1
    if begin >= end:
        return
    pivot = partition(array, begin, end)
    quicksort(array, begin, pivot-1)
    quicksort(array, pivot+1, end)
	
def main():
	rev_deck = {}
	nums = None
	for line in sys.stdin:
		(letter,nums) = line.strip().split(':')
		nums = list(map(int, nums.split(',')))
		for n in nums:
			rev_deck[n]=letter
			print(letter, '...', n)
			
	# print (rev_deck)

	int_list = [v for v in rev_deck]
	#print(int_list)
	#QuickSort(int_list,0,len(int_list)-1)
	quicksort(int_list)
	#print(int_list)
	word = ''
	for q in int_list:
		word+=rev_deck[q]
	print (word)
	
start = timeit.default_timer()
main()
stop = timeit.default_timer()
print (stop-start)