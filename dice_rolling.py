# Roll of Dice

import math
import random

# introduction
print("Welcome to Roll of the Dice!\n")
print("Rules: ")
print("Guess the number on the dice between 1-6.")
print("If you guess correctly, you get 6 points.")
print("If you get it wrong, you lose 1 point.\n")

rounds = input("How many rolls do you want to play?")
print("You will be playing " + rounds + " rounds.")
rollcounter = 1 # number of rounds
pointscore = 0 # score counter

print("Round: " + str(rollcounter))

while str(rounds) != str(rollcounter): # while the game is not over
    random_number = random.randint(1,6) # random number generator between 1-6
    user_guess = int(input("Guess a number between 1-6:"))
    if(user_guess == random_number):
        print("You guessed correctly which was: " + str(random_number))
        pointscore += 6
        print("You now have " + str(pointscore) + " points.")
        command = input("Continue? y/n")
        if command == 'y':
            rollcounter += 1
            print("Round: " + str(rollcounter))
        else: # user doesn't want to continue playing 
            break
    else:
        print("You guessed " + str(user_guess) + " which is incorrect!")
        print("The number was: " + str(random_number))
        pointscore -= 1
        print("You now have " + str(pointscore) + " points.")
        command = input("Continue? y/n")
        if command == 'y':
            rollcounter += 1
            print("Round: " + str(rollcounter))
        else: # user doesn't want to continue playing 
            break

print("You played " + str(rollcounter) + " rounds.")
print("Your total score is: " + str(pointscore) + " points.")
print("Thanks for playing!")