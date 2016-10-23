# ratatosk

from sys import stdin

def dfs(graph, start, ratatosk, depth=0):
    if start == ratatosk:
        print(depth)
        return
    depth+=1
    for child in graph[start]:
        try:
            dfs(graph, child, ratatosk, depth)
        except: pass
      
# def dfs_paths(graph, start, goal):
    # stack = [(start, [start])]
    # while stack:
        # (vertex, path) = stack.pop()
        # for next in graph[vertex] - set(path):
            # if next == goal:
                # yield path + [next]
            # else:
                # stack.append((next, path + [next]))

# def bfs (graph, start):
    # visited, Q = set(), [start]
    # while Q:
        # vertex = Q.pop(0)
        # print ('vertex =',vertex,'type =',type(vertex))
        # if vertex not in visited:
            # print ('visited:',type(visited))
            # print ('graphtype:',type(graph[vertex]))
            # visited.add(vertex)
            # Q.extend(graph[vertex]-visited)
    # return visited
                
def testing():
    next(stdin)                   # funksjon, skip
    next(stdin)                    # antall noder, skip
    start = stdin.readline().strip()       # start node
    ratatosk = stdin.readline().strip()    # object to find
    graph = dict()                      # make a graph
    for line in stdin:
        nums = line.split()
        graph[nums[0]] = nums[1:]
    dfs(graph, start, ratatosk)
    # print (bfs(graph, start))
    # print(bfs(graph, ratatosk))
    # list(dfs_paths(graph, start, ratatosk))
testing()