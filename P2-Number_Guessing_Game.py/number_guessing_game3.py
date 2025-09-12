#Implement a feature that limits the number of guesses a player can make.

import random

number = random.randint(1,100)
count = 0
limit = 5

while True:
    try:
        if limit == 0:
            print(f"You failed the mission. The number is {number}")
            break 
         
        guess = int(input(f"Guess a number between 1 and 100. You have {limit} attempts left.: "))

        if guess > number:
            print("Too high! Try again")
            count += 1
            limit -=1
        elif guess < number:
            print("Too low! Try again")
            count += 1
            limit -=1
        else:
            print(f"Congratulations! You guessed the number in {count} attempts")
            break
        
    except ValueError:
        print("Please enter a valid number")
        count += 1
    
            
   





    