import json
import random

print("~#--------------#~  FRIENDS  ~#--------------#~")
score = 0
with open("questions.json", 'r+') as f:
    question_list = json.load(f)
    for i in range(10):
        total_questions = len(question_list)
        question = random.randint(0, total_questions - 1)
        print(f'\nQ{i + 1} {question_list[question]["question"]}')
        for option in question_list[question]["options"]:
            print(option)
        answer = input("Enter your answer: ")
        if question_list[question]["answer"][0] == answer[0].upper():
            print("You are correct")
            score += 1
        else:
            print("You are incorrect")
        del question_list[question]
    print(f'FINAL SCORE: {score}')
