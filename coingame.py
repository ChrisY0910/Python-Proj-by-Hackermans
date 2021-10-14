import random

def coinGame():

    print("Instructions Guess which side the coin would fall on! You can have one try!")
    score = 0
    coin = ["Heads" , "Tails"]
    toss = random.choice(coin)

    choice = input("Heads or Tails? : ")

    if choice == toss:
        print("You Win! The coin landed on " + toss)
        score += 1
        print("Your score is " + str(score))
    else:
        print("You Lose! The coin landed on " + toss)
        print("Your score is " + str(score))