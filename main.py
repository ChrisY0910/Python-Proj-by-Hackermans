#Game Menu
import time 
import random
import math
import turtle 

t = turtle.Screen()
t.bgcolor('black')
turtle.speed(0)
for i in range (20): 
  for colurs in ['red', 'cyan', 'green', 'turquoise']:
    turtle.color(colurs)
    turtle.circle(100)
    turtle.left(10)

print("Welcome to Hackerman's Minigames!\n")
print("1: Dice Game") # Harrison Ng
print("2: Coin Flip Game") # Chris Yang
print("3: Math Problem Game") # Partho Nath
print("4: Guessing The Number Game") # Harrison Ng
gamegamegame = int(input("What game would you like to play? Pick 1/2/3/4: "))

if gamegamegame == 1:
  print("Welcome to Roll of the Dice!\n")
  print("Rules: ")
  print("Guess the number on the dice between 1-6.")
  print("If you guess correctly, you get 6 points.")
  print("If you get it wrong, you lose 1 point.\n")

  rounds = input("How many rolls do you want to play?")
  print("You will be playing " + rounds + " rounds.")
  rollcounter = 0 # number of rounds
  pointscore = 0 # score counter

  print("Round: " + str(rollcounter))

  while str(rounds) != str(rollcounter): # while the game is not over
      random_number = random.randint(1,6) # random number generator between 1-6
      user_guess = int(input("Guess a number between 1-6: "))
      if(user_guess == random_number):
          print("You guessed correctly which was: " + str(random_number))
          pointscore += 6
          print("You now have " + str(pointscore) + " points.")
          command = input("Continue? y/n ")
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
          command = input("Continue? y/n ")
          if command == 'y':
              rollcounter += 1
              print("Round: " + str(rollcounter))
          else: # user doesn't want to continue playing 
              break

  print("You played " + str(rollcounter) + " rounds.")
  print("Your total score is: " + str(pointscore) + " points.")
  print("Thanks for playing!")

elif gamegamegame == 2:
  #Coin Game By Chris Yang
  def coinGame():
    print("Instructions Guess which side the coin would fall on! You can have one try!")
    score = 0
    coin = ["Heads" , "Tails"]
    toss = random.choice(coin)

    choice = input("Heads or Tails? : " + "Enter as Heads/Tails: ")

    if choice == toss:
        print("You Win! The coin landed on " + toss)
        score += 1
        print("Your score is " + str(score))
    else:
        print("You Lose! The coin landed on " + toss)
        print("Your score is " + str(score))
            
  coinGame()

elif gamegamegame == 3:
 #The math game by Partho Nath
    #Choice variable decides whether to restart the program or not
    choic = 4
    while choic == 4:
        #Operation Menu
        print("Operations to choose : (write in words) ")
        print("1. Addition")    
        print("2. Subtraction")           
        print("3. Multiplication")           
        print("4. Division \n")          

        #taking operation from user input
        op = input("What operation do you want?\n")
        print("")

        #Difficulty level menu
        print("Difficulty levels to choose :")
        print("Level 1 being 1 Digit problems")          
        print("Level 2 being 2 digit problems")          
        print("Level 3 being 3 digit problems") 
        print("Level 4 being 4 digit problems")     
        print("Level 5 being 5 digit problems")
        print("Level 6 being 6 digit problems") 
        print("Level 7 being 7 digit problems")    
        print("Level 8 being 8 digit problems \n")

        #Taking difficulty level from user
        dlvl = int(input("Please Choose difficulty between the 8 levels ?\n"))
        print("")

        #These variables are used to store random numbers
        r1 = 0
        r2 = 0

        #Correct variable stores the number of correct answers given by user
        correct = 0

        #Starting the timer
        t0= time.perf_counter()

        #For loop to give user 5 questions
        for i in range(0,5):
            #Generating random numbers
            if dlvl == 1:
                r1 = random.randint(1,9)
                r2 = random.randint(1,9)
            elif dlvl == 2:
                r1 = random.randint(10,99)
                r2 = random.randint(10,99)
            elif dlvl == 3:
                r1 = random.randint(100,999)
                r2 = random.randint(100,999)
            elif dlvl == 4:
                r1 = random.randint(1000,9999)
                r2 = random.randint(1000,9999)
            elif dlvl == 5:
              r1 = random.randint(10000, 99999)
              r2 = random.randint(10000, 99999)
            elif dlvl == 6:
              r1 = random.randint(100000, 999999) 
              r2 = random.randint(100000, 999999)
            elif dlvl == 7: 
              r1 = random.randint(1000000, 9999999)  
              r2 = random.randint(1000000, 9999999) 
            elif dlvl == 8:   
              r1 = random.randint(10000000, 99999999)
              r2 = random.randint(10000000, 99999999)  

            #Depending on chosen operation, asking user appropriate questions
            #based on previously generated random variables.
            if op == "Addition":
                print(str(r1) + " + " + str(r2))
                answer = int(input())
                if answer == (r1+r2):
                    correct = correct + 1
            elif op == "Subtraction":
                print(str(r1) + " - " + str(r2))
                answer = int(input())
                if answer == (r1-r2):
                    correct = correct + 1  
            elif op == "Multiplication":
                print(str(r1) + " * " + str(r2))
                answer = int(input())
                if answer == (r1*r2):
                    correct = correct + 1
            elif op == "Division":
                print(wtr(r1) + " / " + str(r2))
                answer = int(input())
                if answer == (r1/r2):
                    correct = correct + 1

        #Counting time required to answer these questions
        t1 = time.perf_counter() - t0

        #printing the result and time taken
        print("Congratulations you have completed "+str(correct)+" right answers. Within " + str(round(t1,2))+ " Seconds.")


elif gamegamegame == 4:
 # introduction and instructions
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

diffculty = int(input("What diffculty do you choose? Enter 1/2/3: "))

if diffculty == 1:
  random_number = (random.randint(1, 100)) # generates random num
  guess_check("1-100")
elif diffculty == 2:
  random_number = (random.randint(1, 1000)) 
  guess_check("1-1000")
elif diffculty == 3:
  random_number = (random.randint(1, 10000)) 
  guess_check("1-10000")