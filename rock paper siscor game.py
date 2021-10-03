import random
print('~~~~~~~~Rock paper scisor game~~~~~~~~')
name = input('Enter the name of the player\n')
print('Hey',name)
user = input("Enter a choice (rock, paper, scissors)\n")
choices = ["rock", "paper", "scissors"]
computer = random.choice(choices)
print(f"\nYou chose {user}, computer chose {computer}.\n")

if user == computer:
    print(f"Both players selected {user}. It's a tie!")
elif user == "rock":
    if computer == "scissors":
        print(f"Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif user == "paper":
    if computer == "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif user == "scissors":
    if computer == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")

        

        
