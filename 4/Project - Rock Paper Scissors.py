import random

rock = """
    ________
---'   _____)
        (_____)
        (_____)
        (____)
---.____(___)
"""

paper = """
    _______
---'   ____)____
        ________)
        _________)
        ________)
---.__________)
"""

scissors = """
    _______
---'   ____)______
            ______)
        __________)
        (____)
---.____(___)
"""

game_variable = ["rock", "paper", "scissors"]

game_images = [rock, paper, scissors]

user_choice = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
)

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
else:
    print("You chose: " + game_variable[user_choice])

    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)

    print("Computer chose: " + game_variable[computer_choice])

    print(game_images[computer_choice])

    if user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose")
    elif computer_choice > user_choice:
        print("You lose")
    elif user_choice > computer_choice:
        print("You win!")
    elif computer_choice == user_choice:
        print("It's a draw")
