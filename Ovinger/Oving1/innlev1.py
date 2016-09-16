from sys import stdin

class Node:
	w = None
	next = None
	def __init__(self, w):
		self.w = w
		self.next = None

def search(node):
	big_w = node.w
	while (node.next is not None):
		if (node.next.w > big_w):
			big_w = node.next.w
		node = node.next
	return big_w
	
first = None
last = None
for line in stdin:
	prev_last = last
	last = Node(int(line))
	if first==None:
		first = last
	else:
		prev_last.next = last
print(search(first))