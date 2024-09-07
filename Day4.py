import random

#rock
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

#paper
paper = '''   
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

#scissors
scissor = '''
    _______
---'   ____)____
          ______)
        __________)
      (____)
---.__(___)
'''

# List of game images
game_images = [rock, paper, scissor]

user_choice = int(input("What do you want? 0 for rock, 1 for paper, 2 for scissor: "))

# Validate the user input before accessing the list
if user_choice < 0 or user_choice >= 3:
    print("You typed an invalid number")
else:
    # Correctly print the user's choice
    print("You chose: ")
    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)
     # Print the computer's choice
    print(f"Computer chose: {game_images[computer_choice]}")

    # Determine the result of the game
    if user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif user_choice == 1 and computer_choice == 0:
        print("You win!")
    elif user_choice == 2 and computer_choice == 1:
        print("You win!")
    elif user_choice == computer_choice:
        print("It is a draw")
    else:
        print("Computer wins")

