from string import ascii_lowercase as validChars
import sys


def numify(A, d):
    i = 0
    for a in A:
        A[i] = ([ord(x)-96 for x in a])
        while len(A[i]) < d:
            A[i].append(0)
        i += 1


def print_dict(D):
    for k,v in D.items():
        print (k,'\t',v)


def clearify(A, d):
    # remove leading 0's
    for item in A:
        while (item[-1]==0):
            del item[-1]


def charify(A, d):
    for arr in A:
        print (''.join(chr(x+96) for x in arr))


def sortify(A, d, BASE = 26):
    C = dict((q,[]) for q in range(BASE+1))
    print_dict(C)
    sub_array = 0
    for i in range (d-1,-1,-1): # go from the last index and upwards
        for subArr in A:
            index = subArr[i]
            C[index].append(subArr)
        print ('--------------')
        print ('Dict:')
        print_dict(C)
        print ('______________')
        print ('The new array:')
        A = [y for x in C.values() for y in x if y != []]
        print (A)
        charify(A,d)
        print ('______________')
        C = dict((q,[]) for q in range(BASE+1))
    print ('Clearing up zeros...')
    clearify(A, d)
    print (A)
    print ('Converting back to chars...')
    charify(A, d)


def main():
    d = int(sys.stdin.readline())
    words = [x.strip() for x in sys.stdin]
    print('ORIGINAL!', words)
    numify(words, d)
    print(words)
    sortify(words, d)

main()