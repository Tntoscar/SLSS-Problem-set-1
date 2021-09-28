# Quiz Creation Activity

#Quiz has 5 questions the user will answer.
#It will keep track of score and give
#a final result

import time
score = 0
score = "diamonds"
print("welcome to the amazing quiz")
time.sleep (0)
print("What is your name?")

user_name = input()
time.sleep(0)
print(f"welcome {user_name}")
time.sleep(0)
print("Your objective is to answer all the questions correctly.")
time.sleep(0)
answer_0 = "yes"
print("Are your ready?")
if input() == answer_0:
    print("good to hear")
else:
    print("well too bad")
time.sleep(0)
print("lets begin")
time.sleep(0)
answer = "Captain America"
print("Whos the first Avenger?")
if input() == answer:
    print("Great job")
else:
    print("sorry it's Captain america")
time.sleep(0)
answer_2 = "Minecraft"
print("what is the popular block game called?")
if input() == answer_2:
    print("great, you know the fact")
else:
    print("It is minecraft")
time.sleep(0)
answer_3 = "I am Groot"
print("what is the only line groot knows from the Marvel universe?")
if input() == answer_3:
    print("That is correct. You really know your Avengers.")
else:
    print("The line is 'I am groot'")
time.sleep(0)
answer_4 = "T series"
print("Who is the most subscribe youtube as of when this quiz is made?")
if input() == answer_4:
    print("You are up to date!")
else:
    print("it is T series. You need to be more up to date.")
time.sleep(0)
answer_5 = "2"
print("What is 1+1-1+1")
if input() == answer_5:
    print("You passed math.")
else:
    print("The answer is 2, you need to work on your math skills.")
