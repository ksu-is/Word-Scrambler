f = open("scrumbledDict.txt",'r')
dic = cPickle.load(f)
f.close()

print dic

scrumbled_word = scrumbled_word.strip()
list2 = scrumbled_word.split(" ")
attempt = raw_input("How many times do you want to play? : ")
attempt = int (attempt)
for line in range(attempt):
	ques = random.choice(list2) 
	ques = ques.strip()
	correct = dic.keys()[dic.values().index(ques)]
	print ques
	ans = raw_input("Answer: ")
	ans = ans.strip()
	if ans == correct:
		print "Accepted!"
	else:
		print "Sorry! WA!"
