#Modify the program so the user can specify how many dice they want to roll.

import random

answer = int(input("How many times you want to roll the dice: "))

for i in range (0,answer):
    a = random.randint(1,6)
    b = random.randint(1,6)
    print (f"({a},{b})")
print("Thanks for playing") 
   