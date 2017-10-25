import random

f = open('scrumbler.txt','r')

message = f.read()

f.close()

def __split__ (message):

	message = message.strip()
	word = message.split(" ")

	f = open('scrumbled_done.txt','w')
	for item in range(len(word)):
		text = list(word[item])
		random.shuffle(text)
		shuffled_word = "".join(text)
		print shuffled_word

		message = f.write(shuffled_word + " ")
		
	#print text
	f.close()

__split__(message)
