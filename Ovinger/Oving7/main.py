#!/usr/bin/python3

from sys import stdin
from collections import defaultdict

# _max = None

store = defaultdict(lambda: None)
num_of_calls = 0

# def extend_table(row, column):
    # global _max
    # _max = map(lambda x: x + ([0] * (column - len(x))), _max + ([[0] * column] * (row - len(_max))))

def sub_iter(W,H,vals,PW,PH,val_i,new_PW,new_PH):
    return moneh(W,H,vals,PW,PH) + val_i + moneh(W,H,vals,new_PW,new_PH)
    
def moneh(_W, _H, values, P_W, P_H):
    global num_of_calls
    high = 0
    if store[(P_H,P_W)] is not None:
        num_of_calls += 1
        return store[(P_W,P_W)]
    # if _max[P_H][P_W] is not None:
        # num_of_calls += 1
        # return _max[P_H][P_W]

    for i in range(len(_W)):
        tmp = 0
        #Test each orientation, with both vertical and horizontal cuts for all bills.
        if _W[i] <= P_W and _H[i] <= P_H:
            tmp = sub_iter(_W,_H,values,P_W-_W[i], P_H, values[i], _W[i], P_H - _H[i])
            if tmp > high:
                high = tmp
        if _W[i] <= P_H and _H[i] <= P_W:
            tmp = sub_iter(_W,_H,values,P_W-_H[i],P_H,values[i],_H[i],P_H-_W[i])
            if tmp > high:
                high = tmp
        if _H[i] <= P_H and _W[i] <= P_W:
            tmp = sub_iter(_W,_H,values,P_W,P_H-_H[i],values[i],P_W-_W[i],_H[i])
            if tmp > high:
                high = tmp
        if _H[i] <= P_W and _W[i] <= P_H:
            tmp = sub_iter(_W,_H,values,P_W,P_H-_W[i],values[i],P_W-_H[i], _W[i])
            if tmp > high:
                high = tmp
    # _max[P_H][P_W] = high
    store[(P_W,P_W)] = high
    return high


def find_max(_W, _H, values, P_W, P_H):
    # global _max
    # _max = None
    # SKRIV DIN KODE HER
    # if _max is None:
        # _max = []
        # for i in range(P_H + 1):
            # _max.append([])
            # for j in range(P_W + 1):
                # _max[i].append(None)
    # if len(_max) <= P_H:
        # extend_table(P_H+1, P_W+1)
    # if len(_max[0]) <= P_W:
        # extend_table(P_H+1, P_W+1)

    return moneh(_W, _H, values, P_W, P_H)


def main():
    _W = []
    _H = []
    values = []
    for triple in stdin.readline().split():
        dim_value = triple.split(':', 1)
        dim = dim_value[0].split('x', 1)
        w = int(dim[0][1:])
        h = int(dim[1][:-1])
        value = int(dim_value[1])
        _W.append(int(w))
        _H.append(int(h))
        values.append(int(value))
    for line in stdin:
        P_W, P_H = [int(x) for x in line.split('x', 1)]

        print((find_max(_W, _H, values, P_W, P_H)))
        print(num_of_calls)


if __name__ == "__main__":
    main()