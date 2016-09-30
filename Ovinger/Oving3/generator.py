from sys import stdin
from itertools import repeat
import timeit

def merge(left, right):
	result, i, j = [], 0, 0
	while i < len(left) and j < len(right):
		if left[i][0] <= right[j][0]:
			result.append(left[i])
			i += 1
		else:
			result.append(right[j])
			j += 1
	return result+left[i:]+right[j:]
	
#Merge Sort
def merge_sort(l):
    cut=int(len(l)/2)
    if len(l)<=1:
        return l
    return merge(merge_sort(l[:cut]),  merge_sort(l[cut:]))

def main():
	decks = []
	for line in stdin:
		(index, csv) = line.strip().split(':')
		decks.append(zip(map(int, csv.split(',')), repeat(index)))
	#int_list = [num for nums in decks for num,letter in nums]
	#etters = [l for letters in decks for num,l in letters]
	# print (''.join(x[1] for x in merge_sort([(x,y) for zips in decks for x,y in zips])))
	print (''.join(s[1] for s in sorted([(x,y) for zips in decks for x,y in zips])))
	
	
start = timeit.default_timer()
main()
stop = timeit.default_timer()
print (stop-start)
