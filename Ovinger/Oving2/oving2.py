from sys import stdin
<<<<<<< HEAD
import timeit
import re
from string import ascii_lowercase
from collections import Counter
'''
OUTPUT:
ha: 0 3
mjau:
m?d: 23
e?: 15 36 39
'''
start = timeit.default_timer()

class Node:
	def __init__(self, chr):
		self.chr = chr
		self.children = []
		
	def add_child(self, child):
		if child not in self.children:
			self.children.append(child)
			
	def get_children(self):
		return self.children
			
	def print_node(self):
		print 'Printing node ', self.chr, '\nChildren: ', self.children


txt = ""
search_words = []
for line in stdin:
	if txt=="":
		txt = line.strip()
	else:
		search_words.append(line.strip())

print 'Given text:\n'+txt
print 'Words to look for:', search_words, '\n'
words = txt.split(' ')

#FIND ALL POSSIBLE ITERATIONS OF A WORD CONTAINING '?'
added_words = []
def check_all(word, container):
	_all = []
	ind = word.index('?')
	for x in ascii_lowercase:
		word = word[:ind]+x+word[ind+1:]
		if word in container and word not in added_words:
			added_words.append(word)
			#return word
			_all.append(word[:ind]+x+word[ind+1:])
	return _all

def find_all_indexes(word):
	indexes = []
	for w in txt:
		
	
for w in search_words:
	print w+':',
	if '?' in w:
		w = check_all(w, words) # is now an array [er, en]
		for subword in w:
			print subword, 
			added_words.append(subword)
	else:
		find_all_indexes(w)
		pass
	print ''
	

stop = timeit.default_timer()
print '\n$$$ RUNTIME', '{0:.10f}'.format(stop-start), 'seconds'
#print [m.start() for m in re.finditer(w, txt)]
=======


txt = ""
nodes = {}
for line in stdin:
	for c in line:
		txt += ' 'if c=='\n' else c

#now we can work with the entire string with correct positions
print txt

ind = 0
for c in txt:
	
>>>>>>> origin/master
