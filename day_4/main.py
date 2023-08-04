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

options = [rock, paper, scissors]

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
if player_choice >2 or player_choice < 0:
    print("You typed an invalid number, you lose!")
else: 
    print(options[player_choice] )

    machine_choice = random.randint(0,2)
    print("Compueter chose:")
    print(options[machine_choice] )


    if player_choice == 0 and machine_choice == 2:
        print("You win! :)")
    elif machine_choice == 0 and player_choice == 2:
        print("You lose :(")
    elif machine_choice > player_choice:
        print("You lose :( ")
    elif player_choice > machine_choice:
        print("You win! :) ")
    elif machine_choice == player_choice:
        print("It's a draw!")