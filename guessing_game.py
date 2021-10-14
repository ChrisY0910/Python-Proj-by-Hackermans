# Guessing Number Game
import random
import math

print("Welcome to the Guessing Number game!")
print("You will be chosen an option for the diffculty of the game.")
print("Try guessing the correct number, it will either tell you the number is too high or too low.")
print("Once you got it, you will be displayed the amount of attempts it took to do so.\n")

# diffculty selection
print("Easy(1): 1 to 100") 
print("Medium(2): 1 to 1000")
print("Hard(3): 1 to 10000")

def guess_check(number_range):
      guesscounter = 1
      guess = int(input("Enter a number between " + number_range + ": "))
      while(guess != random_number):
              if(guess > random_number):
                  print(str(guess) + " is too high!")
                  guess = int(input("Enter a number between " + number_range + ": "))
                  guesscounter += 1
              elif(guess < random_number):
                  print(str(guess) + " is too low!")
                  guess = int(input("Enter a number between " + number_range + ": "))
                  guesscounter += 1
      if(guess == random_number):        
          print("You guessed the right number!")
          print("The number is: " + str(random_number) + "!")
          print("It took " + str(guesscounter) + " attempts!")

    diffculty = int(input("What diffculty do you choose? Enter 1/2/3 (4 to begin math problem): "))

    if diffculty == 1:
        random_number = (random.randint(1, 100)) # generates random num
        guess_check("1-100")
    elif diffculty == 2:
          random_number = (random.randint(1, 1000)) 
          guess_check("1-1000")
    elif diffculty == 3:
          random_number = (random.randint(1, 10000)) 
          guess_check("1-10000")