import sys
import timeit
import collections


def numify(A, d):  # change A to a list of ascii-values, 96 for ('a')
    i = 0
    for a in A:
        A[i] = ([ord(x)-96 for x in a])
        while len(A[i]) < d:
            A[i].append(0)
        i += 1

def clearify(A, d):  # remove leading 0's
    for item in A:
        while item[-1] == 0:
            item.pop()


def charify(A, d):
    for arr in A:
        print (''.join(chr(x+96) for x in arr))


# def sortify(A, d, BASE = 26):
#     C = dict( for q in range(BASE+1))
#     for i in range(d-1, -1, -1):  # go from the last index and upwards
#         for subArr in A:
#             C[subArr[i]].append(subArr)
#         A = [y for x in C.values() for y in x if y != []]
#         C = dict((q,[]) for q in range(BASE+1))
#     clearify(A, d)  # removes 0's
#     charify(A, d)   # prints the words

def prettyprint(D):
    for k,v in D.items():
        print (k,'\t',v)

def sortify(A, d):
    for i in range(d-1, -1, -1):
        A = [x[1] for x in sorted([(arr[i],arr) for arr in A])]
    # print (A)
    clearify(A,d)
    charify(A,d)



def main():
    d = int(sys.stdin.readline())
    words = collections.deque([x.strip() for x in sys.stdin])
    # print (words)
    # print('ORIGINAL!', words)
    numify(words, d)
    # print(words)
    sortify(words, d)


t0 = timeit.default_timer()
main()
t1 = timeit.default_timer()
print (t1-t0)