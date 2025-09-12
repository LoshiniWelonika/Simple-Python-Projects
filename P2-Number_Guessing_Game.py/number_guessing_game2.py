#Allow the user to specify the minimum and maximum values for the number range

import random

number1 = int(input("Enter the minimum number in range: "))
number2 = int(input("Enter the maximum number in range: "))

number = random.randint(number1,number2)
count = 0

while True:
    try:
        guess = int(input(f"Guess a number between {number1} and {number2}: "))

        if guess > number:
            print("Too high! Try again")
            count += 1
        elif guess < number:
            print("Too low! Try again")
            count += 1
        else:
            print(f"Congratulations! You guessed the number in {count} attempts")
            break
        
    except ValueError:
        print("Please enter a valid number")
        count += 1
    
            
   





    