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

# Write your code below this line 👇

games = [rock, paper, scissors]

user = int(
    input("What do you choose ? Type 0 for Rock, 1 for Paper or 2 for Scissors : "))
computer = random.randint(0, 2)

user_choice = games[user]
computer_choice = games[computer]

print(f"{user_choice} \n computer choices: \n {computer_choice}")
if user_choice == 0 and computer_choice == 2:
    print("You win")
elif computer_choice == 0 and user_choice == 2:
    print("You lost")
elif computer_choice > user_choice:
    print("You lost")
elif user_choice > computer_choice:
    print("You win")
elif user_choice == computer_choice:
    print("Draw")
