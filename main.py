# chatBot by Hakim
import time

class Bot:
	def __init__(self, name, owner):
		self.name = name;
		self.owner = owner;

	def reply(self, text):
		print(self.name,end=' >> ')
		for char in text:
			print(char,end='',flush=True)
			time.sleep(0.05)
		print();

	def start_conversation(self):
		while(True):
			question = input("You >> ")
			self.__answer(question)

	def __answer(self, text):
		words = {
			"hi":"Hi, wassup.",
			"hello":"Hello there.",
			"name":f"My name is {self.name}.",
			"doing":"Im ready to help with answering your question about this program.",
			"owner":f"My owner is {self.owner}. He's very smart :D",
			"developer":f"{self.owner} is my lovely developer, he's talented XD",
			"no":"okay.",
			"nothing":"okay, another question please.",
			"okay":"ok.",
			"ok":"Alright.",
			"help":"Sorry, im noob."
			# add more answer
		}
		splited = text.lower().split(" ")
		answered = False
		for txt in splited:
			if txt == "exit" or txt == "bye" or text == "quit":
				self.reply("Goodbye.")
				exit()
			if txt in words:
				self.reply(words[txt])
				answered = True
		if not answered:
			self.reply("Sorry, I don't understand.")


def main():
	bot = Bot(
		name="Hakimcodez",
		owner="Daniel Hakim"
	)
	bot.reply("Hello there.")
	bot.start_conversation();

if __name__ == '__main__':
	main()
