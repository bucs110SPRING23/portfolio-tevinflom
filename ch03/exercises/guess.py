import random

num = random.randrange(11)
guess = int(input("Guess a Number 1-10:" ))
for _ in range(3):
    for i in num: 
        if i == guess :
            print("correct")
            break
        elif i > guess:
            print("too low")
        else:
            print("too high")
