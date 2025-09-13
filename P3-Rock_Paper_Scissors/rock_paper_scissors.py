import random

game_list = {'r':"rock", 'p': "paper", 's':"scissor"}

continue_answer = 'y'

while continue_answer == 'y':
    computer_choice_key, computer_choice_value = random.choice(list(game_list.items()))

    user_choice = input("Rock, paper or scissors? (r/p/s): ").lower()

    if user_choice != 'r' and user_choice != 'p' and user_choice != 's': 
        print("Invalid Choice")

    elif user_choice == 'r':
        if computer_choice_key == 'r':
            print(f"You chose {game_list[user_choice]} \nComputer chose {computer_choice_value}") 
            print("It\'s a tie") 
        elif computer_choice_key == 'p':
            print(f"You chose {game_list[user_choice]} \nComputer chose {computer_choice_value}") 
            print("You win")
        else:
            print(f"You chose {game_list[user_choice]} \nComputer chose {computer_choice_value}") 
            print("You lose")

    elif user_choice == 'p':
        if computer_choice_key == 'p':
            print(f"You chose {game_list[user_choice]} \nComputer chose {computer_choice_value}") 
            print("It\'s a tie") 
        elif computer_choice_key == 'r':
            print(f"You chose {game_list[user_choice]} \nComputer chose {computer_choice_value}") 
            print("You win")
        else:
            print(f"You chose {game_list[user_choice]} \nComputer chose {computer_choice_value}") 
            print("You lose")

    else:
        if computer_choice_key == 's':
            print(f"You chose {game_list[user_choice]} \nComputer chose {computer_choice_value}") 
            print("It\'s a tie") 
        elif computer_choice_key == 'p':
            print(f"You chose {game_list[user_choice]} \nComputer chose {computer_choice_value}") 
            print("You win")
        else:
            print(f"You chose {game_list[user_choice]} \nComputer chose {computer_choice_value}") 
            print("You lose")
    
    continue_answer = input("Do you want to continue?(y/n): ") 

