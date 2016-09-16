from sys import stdin, stderr
import traceback

class Node:
	def __init__(self):
		self.children = {}
		self.pos = []

def bygg(wordlist):
    _root = Node()
    for (word, position) in wordlist:
        node = _root
        for letter in word:
            if not letter in node.children:
                node.children[letter] = Node()
            node = node.children[letter]
        node.pos.append(position)
    return _root

def position(word, ind, node):
    if ind >= len(word):
        pos = node.pos
    elif word[ind] == '?':
        pos = []
        for child in node.children.values():
            pos += position(word, ind + 1, child)
			
    elif word[ind] in node.children:
        pos = position(word, ind + 1, node.children[word[ind]])
    else:
        pos = []
    return pos
	
def main():
	sentence = stdin.readline().split() # THE SENTENCE TO CHECK
	search = stdin.read()				# GET ALL THE REMAINING WORDS
	search = search.split() 			# SPLIT INTO WORDS
	pos = 0
	wordlist = []
	for word in sentence:
		wordlist.append((word,pos))
		pos+=len(word)+1
	#print (wordlist)
	_root = bygg(wordlist)
	for sokeword in search:
		sokeword = sokeword.strip()
		print(sokeword+': ', end='')
		pos = position(sokeword, 0, _root)
		pos.sort()
		for p in pos:
			print(p, end =' ')
		print()

main()