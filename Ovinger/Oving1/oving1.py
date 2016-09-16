from sys import stdin
import timeit

#start=timeit.default_timer()

class Node:
	def __init__(self, w):
		self.w = w
		self.next = None
	def has_next(self):
		return self.next is not None
		
def trace(node):
	# traces a node and returns the biggest weight
	big_w = None
	big = lambda a,b: a if a>b else b
	while node.has_next():
		print node
		big_w = big(node.next.w, node.w)
		node = node.next
	return big_w
		
first = None
last = None
for k in stdin:
	prev_last = last
	last = Node(int(k))
	if first == None:
		first = last
	else:
		prev_last.next = last

#stop = timeit.default_timer()
#print 'biggest weight is ',trace(first)
print (trace(first))
#print 'runtime: ', '{0:.10f}'.format(stop-start), 'seconds'