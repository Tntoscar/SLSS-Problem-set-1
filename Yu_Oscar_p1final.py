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
answer = "captain america"
print("whos the first avenger?")
if input() == answer:
    print("Great job")
else:
    print("sorry it's Captain america")
answer_2 = "minecraft"
print("what is the popular block game called?")
if input() == answer_2:
    print("great, you know the fact")
else:
    print("It is minecraft")
answer_3 = "i am groot"
print("what is the only line groot knows from the Marvel universe?")
if input() == answer_3:
    print("That is correct")
else:
    print("The line is 'I am groot'")
e    
    
