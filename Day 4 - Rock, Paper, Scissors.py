import random

user_input = int(input("Thank you for playing Rock, Paper, Scissors\n"
                       "Enter '0' for Rock, '1' for Paper. or '2' for Scissors: "))
comp_input = random.randint(0, 2)
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

print("\n")

if user_input == 0:
    print("You played Rock")
    print(rock)
elif user_input == 1:
    print("You played Paper")
    print(paper)
elif user_input == 2:
    print("You played Scissors")
    print(scissors)
else:
    print("You didn't input any of the options, You Lose")

if comp_input == 0:
    print("Computer played Rock")
    print(rock)
elif comp_input == 1:
    print("Computer played Paper")
    print(paper)
else:
    print("Computer played Scissors")
    print(scissors)

if user_input == comp_input:
    print("Draw")
elif ((user_input == 0 and comp_input == 2) or (user_input == 1 and comp_input == 0) or
      (user_input == 2 and comp_input == 1)):
    print("You Win!")
elif (not (user_input == 0 and comp_input == 2) or not (user_input == 1 and comp_input == 0) or
      not (user_input == 2 and comp_input == 1)):
    print("You Lose!")
