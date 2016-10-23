from collections import defaultdict
from sys import stdin


def min_coins_greedy(coins, val):
    index = 0
    used = 0
    while val>0:
        if val>=coins[index]:
            over_value = val - val % coins[index]
            used += over_value / coins[index]
            val -= over_value
        else:
            index+=1
    return int(used)
    

cache = dict()  # used to store the results
cache[0] = 0
def min_coins(coins, amount):
    sol = dict()
    my_sol = defaultdict(lambda: -1)
    for j in range (1,amount+1):
        # find min amount of coin changes for each j
        # try every denomination for the last coin
        for k in range(0,len(coins)):
            if coins[k] <= j:
                # divide
                sol[k] = cache[j-coins[k]]
                my_sol[k] = sol[k]+1
        # find minimum for my_sol
        cache[j] = -1
        for k in range(0,len(coins)):
            if my_sol[k] > 0:
                if cache[j] == -1 or my_sol[k < cache[j]]:
                    cache[j] = my_sol[k]
    # print(cache)
    return cache[amount]
    
def can_use_greedy(coins):
    return False
    
coins = []
for c in stdin.readline().split():
    coins.append(int(c))
coins.sort()
# coins.reverse()
method = stdin.readline().strip()
if method == "graadig" or (method == "velg" and can_use_greedy(coins)):
    for amount in stdin:
        print(min_coins_greedy(coins, int(amount)))
else:
    for amount in stdin:
        print (min_coins(coins, int(amount)))