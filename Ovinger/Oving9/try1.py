from sys import stdin
from collections import deque

class Node:
    barn = None 
    ratatosk = None
    nesteBarn = None # bare til bruk i DFS
    def __init__(self):
        self.barn = []
        self.ratatosk = False
        self.dybde = 0

def dfs(rot):
    _stack = deque()
    _stack.append(rot)
    while _stack:
        cur =_stack.popleft()
        if(cur.ratatosk):
            return cur.dybde
        if cur.barn:
            dyb=cur.dybde+1
            for b in cur.barn:
                b.dybde = dyb
            _stack.extendleft(cur.barn)

def dfs_iter(rot, ratatosk):
    S, Q = set(), []
    Q.append(ratatosk)
    while Q:
        u = Q.pop()
        if u in S: continue
        S.add(u)
        Q.extend(rot.barn)
        
        
def bfs(rot):
    _queue = deque()
    _queue.append(rot)
    while _queue:
        cur=_queue.popleft()
        if(cur.ratatosk):
            return cur.dybde
        if cur.barn:
            dyb=cur.dybde+1
            for b in cur.barn:
                b.dybde = dyb
            _queue.extend(cur.barn)



funksjon = stdin.readline().strip()
antall_noder = int(stdin.readline())
noder = []
for i in range(antall_noder):
    noder.append(Node())
start_node = noder[int(stdin.readline())]
ratnode = int(stdin.readline())
ratatosk_node = noder[ratnode]
ratatosk_node.ratatosk = True
for linje in stdin:
    tall = linje.split()
    temp_node = noder[int(tall.pop(0))]
    for barn_nr in tall:
        temp_node.barn.append(noder[int(barn_nr)])

if funksjon == 'dfs':
    print (dfs(start_node))
elif funksjon == 'bfs':
    print (bfs(start_node))
elif funksjon == 'velg':
    if(ratnode>antall_noder/3):
        print (dfs(start_node))
    else:
        print (bfs(start_node))