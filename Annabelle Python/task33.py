
import random
score = 0
number=random.randint(1,100)
guess=int(input("Guess a number between 1-100:"))

ng=abs(number-guess)
print(ng)

if ng == 0:
    print("bang on")
    score += 10

elif ng <=5 :
    print("close")
    score +=5

elif ng <= 10:
    print("okay")
    score +=2

else:
    print("way off")
    score +=0

print(f"the number was {number}")
print(f"the score was {score}")
print(f"Final score {score} /10")