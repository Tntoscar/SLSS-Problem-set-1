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

print("Are your ready?")
if input().lower() == "yes" or "yea":
    print("Good to hear")
else:
    print("Well too bad")
time.sleep(2)
print("Lets begin")


time.sleep(2)


print("Who is the first Avenger?")
if input().lower() == "captain america":
    score = score + 1
    print("Great job")
else:
    print("Sorry it's Captain america")


time.sleep(2)



print("What is the popular block game called?")
if input().lower() == "minecraft":
    score = score + 1
    print("Great, you know the fact")
else:
    print("It is minecraft")


time.sleep(2)



print("What is the only line groot knows from the Marvel universe?")
if input().lower() == "i am groot":
    score =  score + 1
    print("That is correct. You really know your Avengers.")
else:
    print("The line is 'I am groot'")


time.sleep(2)



print("As of making this quiz, who is the most subscribed youtuber?")
if input().lower() == "t series":
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