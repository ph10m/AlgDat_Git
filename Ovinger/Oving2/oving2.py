from sys import stdin


txt = ""
nodes = {}
for line in stdin:
	for c in line:
		txt += ' 'if c=='\n' else c

#now we can work with the entire string with correct positions
print txt

ind = 0
for c in txt:
	