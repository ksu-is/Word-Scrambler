import kivy
import random
import cPickle
from sys import stdin
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen

f = open('scrumbler.txt','r')

message = f.read()

f.close()

def __split__ (message):

	message = message.strip()
	word = message.splitlines()

	f = open('scrumbled_kivy_done.txt','w')
	for item in range(len(word)):
		text = list(word[item])
		random.shuffle(text)
		shuffled_word = "".join(text)
		#print shuffled_word

		message = f.write(shuffled_word + " ")
		
	#print text
	f.close()

__split__(message)


f = open("scrumbled_done.txt",'r')
scrumbled_word = f.read()
f.close()


def __scram_dict__(message, scrumbled_word):
	message = message.strip()
	list1 = message.splitlines()

	scrumbled_word = scrumbled_word.strip()
	list2 = scrumbled_word.split(" ")

	dictionary = dict(zip(list1, list2))
	#print dictionary
	

	f = open("scrumbledDict_kivy.txt", 'w')
	dic = f.write(cPickle.dumps(dictionary))
	f.close


__scram_dict__(message, scrumbled_word)


f = open("scrumbledDict_kivy.txt",'r')
dic = cPickle.load(f)
f.close()

#print dic

scrumbled_word = scrumbled_word.strip()
list2 = scrumbled_word.split(" ")

ques = random.choice(list2)

#label = Label()
#label.text = ques


class PlayScreen(Screen):
	pass

class MainScreen(Screen):
	pass

class PlayScreenApp(App):
	f = open("scrumbledDict_kivy.txt",'r')
	dic = cPickle.load(f)
	f.close()
	#print dic
	scrumbled_word = scrumbled_word.strip()
	list2 = scrumbled_word.split(" ")
	text = StringProperty(random.choice(list2))
	life_bar = StringProperty("||||||||||")

	def khali(self):
		self.st = inp.replace("")

	def submit(self, tx, list2, life_bar):
		ans=tx
		ans=ans.strip()
		self.text = random.choice(list2)
		self.text = self.text.strip()
		self.life_bar = life_bar
		print ans


	def build(self):
		screen_manager = ScreenManager()
		screen_manager.add_widget(PlayScreen(name="play_screen"))
		screen_manager.add_widget(MainScreen(name="main_screen"))
		return screen_manager


scrApp = PlayScreenApp()
scrApp.run()