import random

def RockPaperScissors(player_choice):
    options = ['rock', 'paper', 'scissors']
    comp_choice = random.choice(options)

    if player_choice == comp_choice:
         print("It's a tie. Play again.")
    else:
        if player_choice == 'rock':
            if  comp_choice == 'paper':
                print("Sorry, You lost.")
            elif comp_choice == 'scissors':
                print("Congratulations! You win.")
        if player_choice == 'paper':
            if  comp_choice == 'rock':
                print("Congratulations! You win.")
            elif comp_choice == 'scissors':
                print("Sorry, You lost.")
        if player_choice == 'scissors':
            if  comp_choice == 'paper':
                print("Congratulations! You win.")
            elif comp_choice == 'rock':
                print("Sorry, You lost.")

    
player_choice = input('Rock / Paper / Scissors: ').lower()

while player_choice not in ['rock', 'paper', 'scissors']:
    print('Enter valid option.')
    player_choice = input('Rock / Paper / Scissors: ').lower()

RockPaperScissors(player_choice)