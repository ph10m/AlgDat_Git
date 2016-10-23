def cutRod(price, n):
	val = [0] * (n+1)
	for i in range(1,n+1):
		max_v = -32767
		for j in range(i):
			max_v = max(max_v, price[j] + val[i-j-1])
		val[i] = max_v
	return val[n]
	
def knapSack(W, wt, val, n):
	if n == 0 or W == 0:
		print ('Index = 0, or the bag is empty')
		return 0
		
	if (wt[n-1] > W):
		print ('Too big!')
		return knapSack(W, wt, val, n-1)
	else:
		print ('Comparing:',end='')
		t1 = val[n-1] + knapSack(W-wt[n-1], wt, val, n-1)
		t2 = knapSack(W, wt, val, n-1)
		print(t1,'with',t2)
		return max(t1,t2)
		
v1 = [18, 27, 51, 36, 24, 22, 29, 10, 24, 40]
w1 = [320, 301, 371, 296, 303, 359, 148, 275, 296, 395]

# print(knapSack(740, w1, v1, len(v1)))


widths = [2, 2, 4]
heights = [3, 3, 5]
vals = [5, 4, 16]
x = len(widths)

print(knapSack()