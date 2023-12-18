"""
Problem: You are trapped inside a building and in order to leave, you need to guess the same number that the security guard 
         thinks of, or else you will be trapped there forever. Create a program that is a guessing game between the 
         security guard (computer) and the user. The security guard (computer) would generate a random number between 1 and 50, 
         and the user will have to input a number between 1 and 50. The user will have 15 tries to guess the correct number. 
         If they guess the correct number under 15 tries, the user wins and gets to leave. If not, the user loses and remains 
         trapped in the building. If the user wants to give up, then they can input -1 and will be prompted to quit. 
         If the user quits, then they remained trapped in the building. If the user doesn't quit, then they will be punished 
         for prompting to quit but not quitting. 
"""

# Imported the random namespace from the Python standard library - Will be used to generate the secret number the user needs to guess. 
# Needed random library to use random.choice()
import random

# This function introduces the user to the program, and lists the rules of the game
def introduction(): 
    
    # Welcomes user, lets them know about the situation that is going on. 
    print("Oh no! You are trapped inside of the building! The greedy security guard doesn't allow you to leave!")
    print("The security guard challenges you to a guessing game! Here are his rules.")

    # Displays the title of the Rules for the game (lets user know about the rules)
    print("\nRULES: ")

    # Tells user the first rule of the game
    print("1. Enter a number between 1 and 50.")

    # Tells user the second rule of the game
    print("2. The security guard will guess a random number between 1 and 50.")

    # Tells user the third rule of the game
    print("3. If the numbers are the same, you win and you get to leave. You get 15 attempts to guess the number.")

    # Tells user the fourth rule of the game
    print("4. If you can't guess the number in 15 attempts, then you lose and you will be trapped forever!")

    # Tells user the fifth rule of the game
    print("5. If you want to give up during those 15 attempts, then enter -1.")
    
# Function that determines the security guard's number (secret number that the user has to guess)
def secret_num(): 
    
    # Empty list - will be used to store the numbers from 1-50 
    numbers = [] 

    # For loop - iterates through every number in the range from 1 to 50, since the game only guesses numbers from 1 to 50. 
    for n in range(1, 51): 
        
        # Adds the numbers in the range from 1 to 50 into the empty list (numbers) we created earlier. 
        numbers.append(n)
    
    # random.choice() --> Chooses a random element thats in the list (anywhere in the list) and returns it.
    # Chooses a random number in the list of numbers from 1-50 (this will be the number that the user needs to guess to win)
    computer_num = random.choice(numbers)
    
    # Returns the number that was chosen by the computer, so that we can check if the user matches this number or not. 
    return (computer_num)

# Created a new variable to store the security guard's secret number from the function that it was created in so that it
# can be passed into the next function, which determines whether the user was correct or not with their guess. 
guess_num = secret_num()

# Function that determines whether the user's guess matches the security guard's secret number 
def user_turn(guess_num): 
    
    # Initializes counter variable - will be used to keep track of the amount of times the user has made a guess/attempt
    num_guesses = 0

    # Initializes flag variable (flag variable used to check if the user guessed the security guard's number correctly or not)
    guess = False

    # While condition: This loop runs until they guess the correct number, they decide to give up, or when the user has used up all of their 15 attempts 
    # (ends when condition is false, so when equal to 15, meaning this while loop runs if the user's attempts are under 15 (when the condition is true))
    while num_guesses < 15: 
    
        # Asks user to enter a number between 1 and 50, to see if they guessed the same number as the security guard
        user_guess = int(input("\nEnter a number between 1-50 (Enter -1 to give up): "))
    
        # Counter variable - increments count (adds 1 to variable), whenever user makes a guess 
        num_guesses += 1
        
        # If the user enters -1 to give up trying to guess the number
        if user_guess == -1: 
            
            # Asks user if they want to give up trying to guess the number (to double check if they want to quit or not)
            print("\nDo you want to accept defeat to the security guard? ")
            
            # Prompts user to enter either yes or no to the question asked above
            user_giveup = input("Enter yes or no: ")
            
            # A string variable initialized to yes --> The answer user needs to answer if they want to give up guessing. 
            # Will be used to compare if the user's input to the question is equal to yes. If it is, then program stops running and they give up guessing. 
            # If not, the guessing game will continue. 
            user_gives_up = "yes"
            
            # If the user answers "yes", meaning they want to give up
            if user_giveup == user_gives_up: 
                
                # Tells user that they have given up guessing and that they lost. Also thanks them for playing the game. 
                print("\nYou have accepted defeat. You are trapped forever!")
                
                # Tells user the secuirty guard's secret number so that the user knows what it is. 
                print("The security guard's number was: ")
                print(guess_num)
                
                # Exits out of the while loop, ends execution of the program since user chose to give up and stop playing. 
                break 
            
            # If the user answers "no" or types in anything else besides "yes", meaning they don't want to give up.
            else: 
                
                # Tells user that they have not given up/not lost yet, and they have choosen to keep on playing. 
                print("\nYou have choosen to continue the game")
                
                # Since they decided to waste time by inputting the prompt to give up but not actually giving up, the game
                # punishes the user by taking away one of their attempt. 
                print("Since you chose no, you lose an attempt! Don't play around!")
                
                # Skips the remainder of this if-else statement and goes back to the top of the while loop body 
                # Since the user chose to stay in the game and inputted -1 (prompt to give up), they need to guess a number again
                continue

            
        # Checks if the user's guess is between 1 and 50
        if user_guess < 1 or user_guess > 50: 
        
            # If the user's guess is not between 1 and 50, then it lets them know and tells them to input another number
            # that is between 1 and 50. 
            print("Number is not between 1-50, try again.")
                
            # Tells user amount of attempts they have used so they know the amount of attempts they have remaining
            print("Attempts used: ")
            print(num_guesses)
                
        # If the user's guess is between 1 and 50, then the program continues with its execution
        else: 
            
            # If the user correctly guesses the security guard's secret number
            if user_guess == guess_num: 
                
                # Sets the flag variable to true, since the user guessed the correct number
                guess = True 
                
                # Tells user that their guess was correct
                print("\nYour guess is: " + str(guess))
                
                # A message outputs telling the user that they won the game and congratulates them
                print("\nCongratulations! You won the game! You are free!")
                
                # Tells user the security guard's secret number so that the user knows what it is. 
                print("The security guard's number was: ")
                print(guess_num)
                
                # Exits out of the while loop, ends the execution of the program since user won the game by guessing the 
                # correct number
                break
            
            # If the user doesn't correctly guess the security guard's secret number
            else: 
                
                # If the number that the user inputted for their guess doesn't equal to the security guard's secret number. 
                if user_guess != guess_num : 
                    
                    # Tells user that their guess was wrong (uses flag variable, which was already initialized to false at 
                    # the beginnning of the while loop)
                    print("\nYour guess is: " + str(guess))
                    
                    # Tells user to continue guessing the number. 
                    print("Try again!")
                    
                    # Tells the user the amount of attempts they have used so they know how much attempts they have left
                    print("Attempts used: ")
                    print(num_guesses)
                    
    # If the user uses up all of their 15 attempts
    if num_guesses == 15: 
        
        # Tells user that they have used up all of their attempts and that they lose. Lets them know that it is the 
        # end of the game. 
        print("\nLooks like you have used up all of your attempts. Since you didn't guess the number, you lose!")
        print("You are trapped forever!")
        
        # Outputs the secret number that the security guard chose so user knows what it is. 
        print("The security guard's number was: ")
        print(guess_num)

# Calls the functions in our program to run
if __name__ == '__main__': 
    introduction()
    user_turn(guess_num)


        
    