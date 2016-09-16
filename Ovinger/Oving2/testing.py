from sys import stdin, stderr
import traceback

sentence = stdin.readline().split() # THE SENTENCE TO CHECK
search = stdin.read()				# GET ALL THE REMAINING WORDS
search = search.split() 			# SPLIT INTO WORDS

# PUT ALL WORDS AND THEIR POSITION IN A LIST
dictwords = {}
pos = 0
wordlist = []

for word in sentence:
	if word in dictwords:
		dictwords[word].append(pos)
	else:
		dictwords[word] = [pos]
	pos+=len(word)+1


def find_word(word):
	# reduce the temporary sentence to those words of the same length as the input
	x = [x for x in sentence if len(x)==len(word)]
	#print ('Removed invalid words:',sentence)
	# create a list of the input word and check the indexes of all the posisble words!
	word = list(word)
	indexes = []
	
	for w in x:
		for i in range (len(w)):
			if w[i]!='?' and w[i]==word[i]:
				#print (word, 'matches with', w)
				for i in dictwords[w]:
					if i not in indexes:
						indexes.append(i)
				
	indexes.sort()
	indx = ''
	for ind in indexes:
		indx+=str(ind)+' '
	print (indx.strip())
	
	#print (str(indexes)[1:-1])
		
def main():
	# print ('All words: ')
	# for k,v in dictwords.items():
		# print (k,v)
	# print()
	
	# THE ITEMS WE'RE SEARCHING FOR IN THE DICTIONARY
	for word in search:
		if word in sentence:
			print (word+':',end=' ')
			tmp_list = list(dictwords[word])
			tmp_list.sort()
			for x in tmp_list:
				print (x, end = ' ')
			print ()
		elif '?' in word:
			print (word+':',end=' ')
			find_word(word)
		else:
			print (word+':')
	
main()