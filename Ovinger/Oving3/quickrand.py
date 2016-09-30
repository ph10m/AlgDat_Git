import sys
from random import randint

def partition(array, begin, end):
	#pivot = begin
	pivot = randint(begin,end)
	print('pivot:',pivot)
	print('size (end,begin)',end,begin)
	for i in range(begin+1, end+1):
		if array[i][1] <= array[begin][1]:
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
	return array
	
def main():
	deck = []
	nums = None
	for line in sys.stdin:
		(letter,nums) = line.strip().split(':')
		nums = list(map(int, nums.split(',')))
		for n in nums:
			deck.append((letter,n))
	print(''.join([x[0] for x in quicksort(deck)]))
	
main()