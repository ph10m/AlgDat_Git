sentence = 'heisann jeg heter tore mjau maou mao hei er er en hest'
words = sentence.split()

print (words)

lookingfor = 'm??x'

def search(word, sentence):
	# reduce the temporary sentence to those words of the same length as the input
	sentence = (' '.join([x for x in sentence.split() if len(x)==len(word)])).split()
	
	tmp = word[:word.index('?')] # the word up to the first '?'
	print ('Word up to first "?":',tmp)
	for w in sentence:
		if tmp not in w:
			sentence.remove(w)
		# check the rest of the word
		
	print ('Possible matches (only up to the first "?":',sentence)
	#for q in sentence:
		

def find_word(word):
	# reduce the temporary sentence to those words of the same length as the input
	sentence = [x for x in words if len(x)==len(word)]
	print ('Removed invalid words:',sentence)
	
	# create a list of the input word and check the indexes of all the posisble words!
	word = list(word)
	print (word)
	
	all_matches = []
	
	for w in sentence:
		for i in range (len(w)):
			if w[i]!='?' and w[i]==word[i]:
				print (word, 'matches with', w)
	
find_word(lookingfor)




