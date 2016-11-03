from sys import stdin

def dfs(graph, start, ratatosk, depth=0):
	if start == ratatosk:
		print(depth)
		return
	depth += 1
	for child in graph[start]:
		try: dfs(graph, child, ratatosk, depth)
		except: pass
		
def bfs(graph, start, ratatosk, depth=1):
	for child in graph[start]:
		if child == ratatosk: print (depth); return
	depth += 1
	def checkB(parent):
		for child in parent:
			if child == ratatosk:
				print (depth); return
	# dfs(graph, start, ratatosk)
	
def bfs(graph, start, ratatosk, depth=0):
	visited, Q = set(), [start]
	depth = 0
	while Q:
		node = Q.pop()
		if node == ratatosk:
			print (depth); return
		if node not in visited:
			visited.add(node)
			Q.extend((set(graph[node]) - visited))
		depth += 1
		print ('Depth is now',depth)
			
		
# def bfs(root):
    # root.d = 0
    # q = Queue()
    # q.put(root)
    # while not q.empty():
        # node = q.get()
        # if node.ratatosk:
            # return node.d
        # for child in node.child:
            # child.d = node.d + 1
            # q.put(child)
    
def main(): 
	# func = stdin.readline.strip()
	func = stdin.readline()
	stdin.readline()							#skip first two lines
	start = stdin.readline().strip()		# the root
	ratatosk = stdin.readline().strip()		# find plz
	if start==ratatosk:
		print (start)
	else:
		graph = dict()							# input dict
		for line in stdin:
			nums = line.split()
			graph[nums.pop(0)] = nums          # store the child nodes with parents
		bfs(graph,start, ratatosk)
		
main()