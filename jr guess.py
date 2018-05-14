import random

words = ["secretword","fortnite","homeless","angry","carrot"]
hint1 = ["wisper","battle","nyc","mad","vegitable"]

number = random.randint(0,4)

secretword = words[number]

guess = ""

counter = 0


while True:
    print("Guess the secret word")
    print ("Typ 'hint1' or 'give up' for help")

    guess=input()

    if guess == secretword:
        
        print ("yah")
        break

    elif guess == "hint1":
        print( hint1[number] )

    elif guess == "give up":
        print (secretword)
        break
    
