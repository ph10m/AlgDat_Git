def greedy_find(coins, amount):
	count = 0
	for coin in coins:
		while amount >= coin:
			amount -= coin
			count += 1
	return count
	
def dyn_find(coins, amount):
	pass

coins = [1000, 500, 200, 100, 50, 20, 10, 5, 4, 1]
amount = 8423423
print(greedy_find(coins, amount))