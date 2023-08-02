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

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors\n"))
comp_choice = random.randint(0, 2)

if choice == 0:
    print(rock)
elif choice == 1:
    print(paper)
else:
    print(scissors)

print("Computer chose:")

if comp_choice == 0:
    print(rock)
elif comp_choice == 1:
    print(paper)
else:
    print(scissors)


if choice == 0 and comp_choice == 2:
    print("You win!")
elif comp_choice > choice:
    print("You lose!")
elif choice == comp_choice:
    print("It's a draw")
else:
    print("Invalid input. You lose")

