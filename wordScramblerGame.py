import random
import cPickle
from sys import stdin

f = open('scrumbler.txt','r')

message = f.read()

f.close()

def __split__ (message):

	message = message.strip()
	word = message.splitlines()

	f = open('scrumbled_done.txt','w')
	for item in range(len(word)):
		text = list(word[item])
		random.shuffle(text)
		shuffled_word = "".join(text)
		#print shuffled_word

		message = f.write(shuffled_word + " ")
		
	#print text
	f.close()

__split__(message)

f = open("scrumbler.txt",'r')
word = f.read()
f.close()

f = open("scrumbled_done.txt",'r')
scrumbled_word = f.read()
f.close()


def __scram_dict__(word, scrumbled_word):
	word = word.strip()
	list1 = word.splitlines()

	scrumbled_word = scrumbled_word.strip()
	list2 = scrumbled_word.split(" ")

	dictionary = dict(zip(list1, list2))
	#print dictionary
	

	f = open("scrumbledDict.txt", 'w')
	dic = f.write(cPickle.dumps(dictionary))
	f.close


__scram_dict__(word, scrumbled_word)

 
f = open("scrumbledDict.txt",'r')
dic = cPickle.load(f)
f.close()

#print dic

scrumbled_word = scrumbled_word.strip()
list2 = scrumbled_word.split(" ")
attempt = raw_input("How many times do you want to play? : ")
attempt = int (attempt)
points =0;

for line in range(attempt):
	ques = random.choice(list2) 
	ques = ques.strip()
	correct = dic.keys()[dic.values().index(ques)]
	print "Ques no. ", line+1, ": ", ques
	ans = raw_input("Answer: ")
	ans = ans.strip()

	if ans == correct:
		points = points+1
		print "Accepted! and your point is: ", points
	else:
		print "Sorry! WA! and your point is: ", points
		print "The CA was: ", correct

	print " "


print " "
print "Your final result is: ", points, attempt
print " "

val = float (points) /attempt
avg = val*100
#print avg

if avg == 0:
	print "Damn, you're so bad, cow!!!!!"

elif avg < 20:
	print "Nigga have you ever gone to school?"

elif  avg < 50:
	print "Welcome to school"

elif avg < 75:
	print "Teach the developer some english, he's so bad"

else: 
	print "That'some shit right there, you should write your own dictionary"

