import random


print("\n--------Welcome to Number Guessing Game-----------\n")

attempts=1
rem=10

comp= random.randint(1,100)

while(True):
    
    if(rem==0):
        print("Game Over!")
        break

    user = input("Guess Number(1-100)  OR  Quit (q) : ")
    if(user.lower()=='q'):
        print("Game Over!")
        print(f"Answer: {comp}")
        break
    user=int(user)

    if(user==comp):
        print("Congratulations! You Guessed the correct one!")
        print("You did it attempt: ",attempts)
        break
    if(user<comp):
        print("Less than the correct.")
    else:
        print("Bigger than the correct.")

    attempts+=1
    rem=rem-1
