import random

number = random.randint(1,100)
count = 0

while True:
    try:
        guess = int(input("Guess a number between 1 and 100: "))

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
    
            
   





    