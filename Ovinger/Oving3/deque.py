import sys
import itertools
import collections

def _deq(l,r):
	deq=collections.deque()
	app=deq.append
	pop1, pop2 = l.popleft, r.popleft
	while l and r: app(pop1() if l[0]<=r[0] else pop2())
	deq+=l if l else r
	return deq

def merge(decks):
	_size = len(decks)
	if _size==2:
		return _deq(decks[0],decks[1])
	elif _size==1:
		return decks[0]
	h=_size//2
	return _deq(merge(decks[:h]),merge(decks[h:]))

def main():
	decks = [collections.deque(zip(map(int,nums.split(',')),itertools.repeat(letter))) for (letter,nums) in (line.split(':') for line in sys.stdin)]
	# print(decks)
	print(''.join(x[1] for x in merge(decks)))

main()