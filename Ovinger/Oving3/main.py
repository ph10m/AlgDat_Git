import sys
import itertools

# def merge(deck, size):
	# word = size*[None]
	# for k in deck:
		# for q in k:
			# word[q[0]-1]=q[1]
		# #arrays
	# print (''.join(word))

	
def merge(deck,_size):
	word = _size*[None]
	for k in deck:
		_letter = k[0][1]
		for i in k:
			word[i[0]-1]=(i[0],_letter)
	
	print (''.join([x[1] for x in word]))
	#print (word)
	return [word]

def main():
	decks = []
	_app = decks.append
	_size = 0
	for line in sys.stdin:
		(letter, nums) = line.strip().split(':')
		box = list(zip(map(int, nums.split(',')),itertools.repeat(letter)))
		_size+=len(box)
		_app(box)
	print("FROM INPUT:\n",decks,'\n')
		# decks.append(deck)
	decks = merge(decks,_size)
	
	print("\nAFTER MERGE:\n",decks)

# def main():
	# deck = {}	
	# # arr_size = (print(''.join(n for n in sys.stdin.read().split(':'))))
	# nums = ''
	# _size = 0
	# for line in sys.stdin:
		# #print (line)
		# (letter,nums) = line.strip().split(':')
		# nums = nums.replace(',','')
		# _size+=len(nums)
		# deck[letter] = list(nums)
	# word = _size*[None]
	
	# for k,v in deck.items():
		# for i in map(int,v):
			# word[i-1]=k
			
	# print ''.join(word)
		

main()