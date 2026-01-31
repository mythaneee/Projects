import random

answer = random.randint(1,100)
attempt = 0      
guesses = []                                                                   # set guesses & attempts to 0 so it can be added
attempts = []
max_attempts = 10
total_games = 0
total_score = 0
is_running = True or False

while is_running == True:
    print(f"Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between 1 and 100")
    
    while attempt < 10:
        try:
            guess = input("Enter your guess: ")
            guesses.append(guess)                                                       # collates guesses made in each attempt
            guessque = int(guess)                                                       # turns guess into an int()
            attempts.append(attempt)                                                    # collates total no. of attempts 
        except ValueError:                                                              # only accepts number as an attempt
             print(f"Please try again!")
             continue 
             if guessque == answer or attempt == 10:
              break
             

        if guessque == answer:
            print(f"You got it! The number was {answer}!")
            attempt += 1
            print(f"You took {attempt} attempt{'s' if attempts != 1 else ''}.")
            break                                                                   # the line that stops further guesses
            
        elif guessque > answer:
            print(f"Too high!")
            attempt += 1                                                            # adds each attempt made
            print(f"Attempt {attempt}/10")

        elif guessque < answer:
                print(f"Too low!")
                attempt += 1
                print(f"Attempt {attempt}/10")

    if attempts == "10" or breakpoint:
            print(f"Your guesses were: {guesses}")
            print(f"Thank you for playing!")

# adds up after attempts used or won
    total_games = total_games + 1                                                   
    
     # scoring
    if guessque == answer:                                                         
        if attempt <= 3:
            points = 5
        elif attempt <= 7:
            points = 3
        else :
            points = 1
    else :
         points = 0

    total_score = total_score + points

    play_again = input("Play again? (yes/no): ") 
    if play_again == "yes":
         is_running == True
         attempt = 0       
         guesses = []                                                                   # resets variables
         attempts = []
         answer = random.randint(1,100)

    else :
         play_again != "yes"
         is_running == False
         print(f"Thank you for playing!")
         print(f"You played {total_games} game{'s' if {total_games} != 1 else ''}.")
         print(f"Your total score: {total_score}")
         break
     
