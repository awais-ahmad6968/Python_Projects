import random
choice_Dict={
    "s":1,
    "w":2,
    "g":3,
    1:"s",
    2:"w",
    3:"g"
}

userChoice=input("Enter Your choice ('s','w','g') : ")
you = choice_Dict[userChoice]

comp= random.randint(1,3)
compChoice=choice_Dict[comp]

print("You chose: ",userChoice)
print("Computer chose: ",compChoice)

if(comp==you):
    print("Draw!")
  
elif(comp==1 and you==2):
    print("Computer Wins")
elif(comp==1 and you==3):
    print("You win")
elif(comp==2 and you==1):
    print("You win")
elif(comp==2 and you==3):
    print("Computer Wins")
elif(comp==3 and you==1):
    print("Computer Wins")
elif(comp==3 and you==2):
    print("You win")
else:
    print("Error!")