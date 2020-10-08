import json
import random

print("~#--------------#~  FRIENDS  ~#--------------#~")
score = 0
number_of_question = 5
with open("questions.json", 'r') as f:
    question_list = json.load(f)
    for i in range(number_of_question):
        total_questions = len(question_list)
        # print(total_questions)
        question = random.randint(0, total_questions - 1)
        print(f'\nQ{i + 1}. {question_list[question]["question"]}')
        for option in question_list[question]["options"]:
            print(option)
        answer = input(">>> Enter your answer: ")
        if question_list[question]["answer"][0] == answer[0].upper():
            print("＼(*ﾟ∀ﾟ*)／ You were right!")
            score += 1
        else:
            # print("Close but not quite... ヾ(￣◇￣)ノ")
            print("ヾ(￣◇￣)ノ Hmm close but not quite... ")
        del question_list[question]
    print("\nYour score is", score)
