import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors\n"))
if choice >= 3 or choice < 0:
    print("Invalid choice. You lose!")
else:

    print(game_images[choice])


    print("Computer chose:")
    comp_choice = random.randint(0, 2)
    print(game_images[comp_choice])



    if choice == 0 and comp_choice == 2:
        print("You win!")
    elif choice == 1 and comp_choice == 0:
        print("You win!")
    elif choice == 2 and comp_choice == 0:
        print("You lose!")
    elif choice == 2 and comp_choice == 1:
        print("You win!")
    elif comp_choice > choice:
        print("You lose!")
    elif choice == comp_choice:
        print("It's a draw")


