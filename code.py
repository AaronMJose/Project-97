import random
print("Number Guessing Game")
number=random.randint(1,9)
chances=0
print("Guess a number(betweem 1 and 9)")
while chances < 5:
    guess=int(input("enter your guess-<"))
    if guess==number:
        print("Congratulation! you won")
    elif guess<number:
        print("Your guess was too low!:guess a number higher then,",guess)
    else:
        print("Your guess was too high!:guess a number lower then,",guess)         
    chances+=1
if not chances > 5:
    print("You Lose!The number is,",number)               