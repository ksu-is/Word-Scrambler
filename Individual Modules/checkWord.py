import random
import cPickle

f = open("scrumbledDict.txt",'r')
dic = cPickle.load(f)
f.close()

#print dic

scrumbled_word = scrumbled_word.strip()
list2 = scrumbled_word.split(" ")

#attempt = raw_input("How many times do you want to play? : ")
#attempt = int (attempt)

points = 0
attempt = 0
lives = 5
wa = 0
line = 0

while (lives != 0):
	attempt = attempt + 1
	line = line + 1

	ques = random.choice(list2) 
	ques = ques.strip()

	correct = dic.keys()[dic.values().index(ques)]

	print "Ques no. ", line, ": ", ques
	ans = raw_input("Answer: ")
	ans = ans.strip()

	if ans == correct:
		points = points+1
		print "Accepted! and your point is: ", points, "Lives = ", lives 

	else:
		wa = wa + 1 
		if(wa % 2 == 0):
			lives = lives - 1
		print "Sorry! WA! and your point is: ", points, "Lives = ", lives
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
	print "That's some shit right there, you should write your own dictionary"
