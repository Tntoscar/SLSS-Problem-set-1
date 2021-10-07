# Quiz Creation Activity

#Quiz has 5 questions the user will answer.
#It will keep track of score and give
#a final result

import time
score = 0
print("Welcome to the amazing quiz")
time.sleep (2)
print("What is your name?")

user_name = input()
time.sleep(2)
print(f"Welcome {user_name}")
time.sleep(0)
print("Your objective is to answer all the questions correctly.")
time.sleep(2)
answer_0 = "yes"
answer_01 = "yea"
print("Are your ready?")
if input() == answer_0 or answer_01:
    print("Good to hear")
else:
    print("Well too bad")
time.sleep(2)
print("Lets begin")
time.sleep(2)
answer = "Captain America"
answer2 = "captain america"
print("Who is the first Avenger?")
if input() == answer or answer2:
    score = score + 1
    print("Great job")
else:
    print("Sorry it's Captain america")
time.sleep(2)
answer_2 = "Minecraft"
answer2_2 = "minecraft"
print("What is the popular block game called?")
if input() == answer_2 or answer2_2:
    score = score + 1
    print("Great, you know the fact")
else:
    print("It is minecraft")
time.sleep(2)
answer_3 = "I am Groot"
answer2_3 = "i am groot"
print("What is the only line groot knows from the Marvel universe?")
if input() == answer_3 or answer2_3:
    score =  score + 1
    print("That is correct. You really know your Avengers.")
else:
    print("The line is 'I am groot'")
time.sleep(2)
answer_4 = "T series"
answer2_4 = "t series"
print("As of making this quiz, who is the most subscribed youtuber?")
if input() == answer_4 or answer2_4:
    score = score + 1
    print("You are up to date!")
else:
    print("It is T series. You need to be more up to date.")
time.sleep(2)
answer_5 = "2"
print("What is 1+1-1+1")
if input() == answer_5:
    score = score + 1
    print("You passed math.")
else:
    print("The answer is 2, you need to work on your math skills.")
if score == 5:
    print(f"Well done your passed the quiz. Your score is {score}/5")
if score == 4:
    print(f"So close, try again later. your score is {score}/5")
if score == 3:
    print(f"Try again after you study. Your score is {score}/5")
if score == 2:
    print(f"You still need to study more. Your score is {score}/5")
if score == 1:
    print(f"If you wish to beat this quiz, train for another 100 years. your score is {score}/5")