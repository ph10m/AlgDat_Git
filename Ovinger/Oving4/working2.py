import sys
def quick_sort_iterative(list_, left, right):
    """
    Iterative version of quick sort
    """
    temp_stack = []
    temp_stack.append((left,right))
    
    #Main loop to pop and push items until stack is empty
    while temp_stack:      
        pos = temp_stack.pop()
        right, left = pos[1], pos[0]
        piv = partition(list_,left,right)
        #If items in the left of the pivot push them to the stack
        if piv-1 > left:
            temp_stack.append((left,piv-1))
        #If items in the right of the pivot push them to the stack
        if piv+1 < right:
            temp_stack.append((piv+1,right))
 
def partition(list_, left, right):
    """
    Partition method
    """
    #Pivot first element in the array
    piv = list_[left]
    i = left + 1
    j = right
 
    while 1:
        while i <= j  and list_[i] <= piv:
            i +=1
        while j >= i and list_[j] >= piv:
            j -=1
        if j <= i:
            break
        #Exchange items
        list_[i], list_[j] = list_[j], list_[i]
    #Exchange pivot to the right position
    list_[left], list_[j] = list_[j], list_[left]
    return j

def binsearch(A,val):
	lo, hi, last = 0, len(A)-1, 0
	while lo<=hi:
		mid = (lo+hi)//2
		last = mid
		if val<A[last]:
			hi = mid-1
		elif val>A[last]:
			lo = mid+1
		else:
			return last
	return last

def find(A, _min, _max):
	lim = [0,0]
	a = binsearch(A,_min)
	lim[0] = A[a-1] if A[a]>_min and a!=0 else A[a]
	b = binsearch(A,_max)
	if b == len(A):
		b -= 1
	elif A[b]<_max and b<len(A)-1:
		b += 1
	lim[1] = A[b]
	return str(lim[0])+" "+str(lim[1])
	
	
def main():
	sorted = [int(x) for x in sys.stdin.readline().split()]
	# A = [int(x) for x in sys.stdin.readline().split()]
	quick_sort_iterative(sorted,0,len(sorted)-1)
	for line in sys.stdin:
		line = line.split()
		print(find(sorted, int(line[0]),int(line[1])))
		
main()