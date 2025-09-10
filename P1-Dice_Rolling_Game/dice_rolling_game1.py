#Add a feature that keeps track of how many times the user has rolled the dice during the session. 

import random

i = 0
while True:
    answer = input("Roll the Dice: ").lower()

    if answer == "y":
        a = random.randint(1,6)
        b = random.randint(1,6)
        print (f"({a},{b})")
        i += 1
    elif answer == "n": 
        print (f"Thanks for playing! You rolled the dice {i} times")
        break
    else:
        print("Invalid choice!")
    