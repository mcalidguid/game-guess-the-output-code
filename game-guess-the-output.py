import json
import random
import getpass

def menu():
	print("\n==========QUIZ START==========")
	score = 0
	with open("questions.json", 'r+') as f:
		question_list = json.load(f)
		for i in range(10):
			number_of_questions = len(question_list)
			question = random.randint(0, no_of_questions-1)
			print(f'\nQ{i+1} {question_list[question]["question"]}\n')
			for option in question_list[question]["options"]:
				print(option)
			answer = input("\nEnter your answer: ")
			if question_list[question]["answer"][0] == answer[0].upper():
				print("\nYou are correct")
				score+=1
			else:
				print("\nYou are incorrect")
			del question_list[question]
		print(f'\nFINAL SCORE: {score}')