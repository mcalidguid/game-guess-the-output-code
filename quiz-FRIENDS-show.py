import json
import random

print("""-------------------------------------------------------------------
~#--------------#~  Are You A True FRIENDS Fan?  ~#--------------#~
-------------------------------------------------------------------
It’s been 25 years since the show aired and we’re still watching it. 
Either way, do you know enough about Friends? Let’s find out!
  Choose level of difficulty:
    Enter \'1\' for Easy \"I think so. I have watched FRIENDS!\"
    Enter \'2\' for Medium \"You bet! I know enough about FRIENDS.\"
    Enter \'3\' for Hard \"Ahaa! I'm a true FRIENDS superfan!\"
    Enter \'4\' for Quit \"Dang! I'm scared!\"
-------------------------------------------------------------------""")
user_input = int(input(">>>: "))
    if user_input == 1:
        number_of_question = 5

    elif user_input == 2:
        number_of_question = 10

    elif user_input == 3:
        number_of_question = 20

    elif user_input == 4:
        exit()

    else:
        print("Invalid input.")


score = 0
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
