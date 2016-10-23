from collections import defaultdict
table = defaultdict(int)
table[0] = 1
def count(S, m, n):
    if n in table:
        return table[n]
    for i in range(m):
        for j in range (S[i], n+1):
            table[j] += table[j-S[i]]
            print (j,':',table[j])
        print ()
    print (table)
    return table[n]
coins = [1000, 500, 200, 100, 50, 20, 10, 5, 4, 1]
m = len(coins)
n = 8 #(1x 20, 1x 5, 1x4, 3 coins)
print (count(coins, m, n))