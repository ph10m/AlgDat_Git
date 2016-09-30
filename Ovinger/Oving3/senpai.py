from sys import stdin
from itertools import repeat
from collections import deque
import timeit

def m2(l1,l2):
    deq=deque()
    app=deq.append
    pop1=l1.popleft
    pop2=l2.popleft
    while l1 and l2:
        app(pop1() if l1[0] <= l2[0] else pop2())
    deq+=(l1 if l1 else l2)
    return deq

def merge(decks):
	_size = len(decks)
	if _size==2:
		return m2(decks[0],decks[1])
	elif _size==1:
		return decks[0]
	else:
		h=_size//2
		return m2(merge(decks[:h]),merge(decks[h:]))

def main():
	decks = []
	app=decks.append
	for line in stdin:
		(index, csv) = line.strip().split(':')
		app(deque(zip(map(int, csv.split(',')), repeat(index))))
	#print("".join(map(lambda x: x[1],merge(decks))))
	print(''.join(x[1] for x in merge(decks)))
	merge(decks)


start = timeit.default_timer()
main()
stop = timeit.default_timer()
print ('\n$$$ RUNTIME', '{0:.10f}'.format(stop-start), 'seconds')