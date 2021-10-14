 #importing the Necessary Modules
    import random
    import time

    #Choice variable decides whether to restart the program or not
    choice = 0
    while choice == 0 :
        #Operation Menu
        print("Operations to choose : ")
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

        #Asking user whether to restart the program or not
        choice = int(input("Press 0 to restart the program. Or else press any key."))