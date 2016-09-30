import sys
# import itertools
#from random import randint
# import timeit

def qsort(L):
    return (qsort([y for y in L[1:] if y <  L[0]]) + 
            L[:1] + 
            qsort([y for y in L[1:] if y >= L[0]])) if len(L) > 1 else L
			
# def quickSort(arr): #modified to look at the secondary of a tuple
	# less = []
	# pivotList = []
	# more = []
	# if len(arr) <= 1:
		# return arr
	# else:
		# pivot = arr[0][1]
		# for i in arr:
			# if i[1] < pivot:
				# less.append((i[0],i[1]))
			# elif i[1] > pivot:
				# more.append((i[0],i[1]))
			# else:
				# pivotList.append((i[0],i[1]))
		# less = quickSort(less)
		# more = quickSort(more)
		# return less + pivotList + more
		
def main():
	deck = []
	_app = deck.append
	nums = None
	
	word = {}
	for line in sys.stdin:
		(letter,nums) = line.strip().split(':')
		for n in nums.split(','):
			word[int(n)]=letter
	wd = ''
	for x in qsort([v for v in word]):
		wd += word[x]
	print(wd)
	# print (''.join([word[x] for x in qsort([v for v in word])]))
	#print(word)
	#test = qsort(deck)
	
# start = timeit.default_timer()
main()
# stop = timeit.default_timer()
# print (stop-start)