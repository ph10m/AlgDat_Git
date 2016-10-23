from sys import stdin
from collections import defaultdict

def maxValue(_W, _H, _V, P_W, P_H):
    result = defaultdict(lambda: [0])
    for w in range(P_W + 1):
        result[w] = [-1] * (P_H+1)
    minSize = min(_W,_H)
   
    for x in range(len(_V)):
        if _W[x] <= P_W and _H[x] <= P_H and result[_W[x]][_H[x]] < _V[x]:
            result[_W[x]][_H[x]] = _V[x]
        if _H[x] <= P_W and _W[x] <= P_H and result[_H[x]][_W[x]] < _V[x]:
            result[_H[x]][_W[x]] = _V[x]
    
    for w in range(P_W + 1):
        for h in range(P_H + 1):
            if result[w][h] == -1:
                best = 0
            else:
                best = result[w][h]
            for vertical in range(1, w):
                if best < result[vertical][h] + result[w - vertical][h]:
                    best = result[vertical][h] + result[w - vertical][h]
            for horiz in range(1, h):
                if best < result[w][horiz] + result[w][h - horiz]:
                    best = result[w][horiz] + result[w][h - horiz]
            result[w][h] = best
    return result[P_W][P_H]

_W = []
_H = []
_V = []
for triple in stdin.readline().split():
    dim_value = triple.split(':', 1)
    dim = dim_value[0].split('x', 1)
    width = int(dim[0][1:])
    height = int(dim[1][:-1])
    value = int(dim_value[1])
    _W.append(int(width))
    _H.append(int(height))
    _V.append(int(value))
for line in stdin:
    P_W, P_H = line.split('x', 1)
    print (maxValue(_W, _H, _V, int(P_W), int(P_H)))