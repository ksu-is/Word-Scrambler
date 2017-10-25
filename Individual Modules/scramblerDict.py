import cPickle

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
