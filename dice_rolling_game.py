import random

while True:
    answer = input("Roll the Dice: ").lower()

    if answer == "y":
        a = random.randint(1,6)
        b = random.randint(1,6)
        print (f"({a},{b})")
    elif answer == "n": 
        print ("Thanks for playing!")
        break
    else:
        print("Invalid choice!")
    