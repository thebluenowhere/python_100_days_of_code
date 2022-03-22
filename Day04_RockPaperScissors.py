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

#Write your code below this line 👇

import random

moves = [rock, paper, scissors]

# Player choice
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors. "))

if choice == 0:
  print(moves[0])
elif choice == 1:
  print(moves[1])
elif choice == 2:
  print(moves[2])
else: 
  quit(print("\nNot a valid choice\n"))
  

# Computer 'choice'

bot = random.randint(0, (len(moves) -1))

print(f"Computer chose:\n{moves[bot]}")

# Rules for win

if choice == 0 and bot == 2:
  print("You win")
elif choice == 1 and bot == 0:
  print("You win")
elif choice == 2 and bot == 1:
  print("You win")
elif choice == bot:
  print("It's a draw.")
else: 
  print("You lose.")
