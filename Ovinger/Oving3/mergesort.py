from sys import stdin
from itertools import repeat
import timeit

def combine(left, right):
    output,i,j =[],0,0
    outputSize = len(left) + len(right)
    left.append((float("inf"), ''))
    right.append((float("inf"), ''))
    while len(output) < outputSize:
        if left[i][0] > right[j][0]:
            output.append(right[j])
            j += 1
        else:
            output.append(left[i])
            i += 1
    return output

def merge(decks):
    while len(decks) > 1:
        decks[0] = combine(decks[0],decks[-1])
        decks.remove(decks[-1])
    return ''.join(x[1] for x in decks[0])


def main():
	decks = []
	for line in stdin:
		(index, csv) = line.strip().split(':')
		deck = list(zip(map(int, csv.split(',')), repeat(index)))
		decks.append(deck)
	#print(decks)
	#print(merge(decks))

start = timeit.default_timer()
main()
stop = timeit.default_timer()
print (stop-start)
