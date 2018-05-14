import random
import time


number = random.randint (1, 100)

guess = 0

counter = 0

while True:
    counter += 1
    print ("guess my number beetween 1 and 100!")
    guess = int(input())

    if number == guess:
        print("you got a freind in me")
        print("you took " + str (counter) + " guesses")
        break 


    elif guess > number:
        print("your high")

    
    elif guess < number:
        print("your low")
