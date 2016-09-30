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

def split_q(q,start,end):
	return collections.deque(itertools.islice(q,start,end))

def merge(decks):
	_size = len(decks)
	DEQ = collections.deque
	if _size==2:
		return _deq(DEQ([decks[0]]), DEQ([decks[1]]))
	elif _size==1:
		return DEQ([decks[0]])
	h=_size//2
	return _deq(merge(split_q(decks,0,h)),split_q(decks,h,_size))

def main():
	deq = collections.deque()
	for (letter,nums) in (line.split(':') for line in sys.stdin):
		deq+=(zip(map(int,nums.split(',')),itertools.repeat(letter)))
	print(''.join(x[1] for x in merge(deq)))

main()