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

store = {}
def min_coins(coins, val):
    tmp_store = {}
    if val in store:
        # print ('used store!')
        return store[val]
    start_val = val
    index = 0
    used = 0
    # print ('\nChecking',val)
    greedy_result = 0
    dyn_result = 0
    while val > 0:
        if val >= coins[index]:
            over_val = val - val % coins[index]         # 9000 (nearest coin)
            if over_val in store:
                # print ('used store inside')
                used += store[over_val]
            else:
                step_used = int(over_val / coins[index])    # 9 used of nearest coin
                tmp_store[over_val] = step_used
                used += step_used
            val -= over_val
        index += 1
    greedy_result = used
    
    val = start_val
    index = 0
    used = 0
    value_left = val % coins[index]
    # check if the next coins yields a better result
    while value_left > 0 and index < len(coins):
        index+=1
        value_left = val % coins[index]
    used = int(val / coins[index])                    
    dyn_result = used
        
    if dyn_result < greedy_result:
        # print ('dynamic result better!')
        store[val]=dyn_result
        return dyn_result
    else:
        # print ('greedy result best!')
        store[val] = greedy_result
        store.update(tmp_store)
        return greedy_result

def can_use_greedy(coins):
    # bare returner False her hvis du ikke klarer aa finne ut
    # hva som er kriteriet for at den graadige algoritmen skal fungere
    # SKRIV DIN KODE HER
    return False

coins = []
for c in stdin.readline().split():
    coins.append(int(c))
coins.sort()
coins.reverse()
method = stdin.readline().strip()
if method == "graadig" or (method == "velg" and can_use_greedy(coins)):
    for amount in stdin:
        print(min_coins_greedy(coins, int(amount)))
else:
    for amount in stdin:
        print (min_coins(coins, int(amount)))