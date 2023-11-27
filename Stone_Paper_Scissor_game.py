# The project no.2
# Project name : Stone_Paper_sciscors game ! 
# Here , The user considered as a player and he needs to give an input ,which is compared to the computer input and shows the result.
# import random module to choose randoms !
import random
Won = 0
Loss = 0
Tie = 0
# Set the Conditions for the game ! or calculate the scenarios !
def check(Player_1,Computer):
        global Won
        global Loss
        global Tie       
        if Player_1 == 'stone' and Computer == 'stone':
            j.append('Tie')
            Tie += 1
            return 'The match result is : Tie' 
        elif Player_1 == 'stone' and Computer == 'paper':
            j.append("Computer Win")
            Loss += 1
            return "The match result is : Computer Win"
        elif Player_1 == 'stone' and Computer == "scissor":
            j.append("Player win")
            Won += 1
            return "The match result is : Player win"
        elif Player_1 == 'paper' and Computer == 'paper':
            j.append('Tie')
            Tie += 1
            return 'The match result is : Tie'
        elif Player_1 == 'paper' and Computer == 'stone':
            j.append("Player win")
            Won +=1
            return "The match result is : Player win"
        elif Player_1== 'paper' and Computer == "scissor":
            j.append("Computer Win")
            Loss += 1
            return "The match result is : Computer Win"
        elif Player_1 == "scissor" and Computer =="scissor":
            j.append('Tie')
            Tie += 1
            return 'The match result is : Tie'
        elif Player_1 == "scissor" and Computer == 'stone':
            j.append("Computer Win")
            Loss += 1
            return "The match result is : Computer Win"
        elif Player_1 == "scissor" and Computer == 'paper':
            j.append("Player win")
            Won += 1
            return "The match result is : Player win"

# Let the players to play the game !
print("Welcome to the '#_Stone Paper Scissor Game' ")
# gather total number of rounds user wants to play
n = int(input('Enter the total number of rounds you want to play : '))
j =[]
c = ['stone','paper','scissor']
print('''
Enter 1 for " Stone "
Enter 2 for " Paper "
Enter 3 for " scissor "
pick anyone among these 3 .
make sure your inputs are numbers \n''')
# Process the operation!
for i in range(1,n+1):
    try: # Exception block
        Player_1 = int(input(f'Game no.{i}  Enter your choice : ')) 
    except Exception as e: 
        print('Enter only numbers') 
# Assign the values for the computer_player !
    Computer = random.choice(c)
    if Player_1 == 1:
        Player_1 = 'stone'
    elif Player_1 == 2:
        Player_1 = 'paper'
    elif Player_1 == 3:
        Player_1 = "scissor"
    else:
        print('Enter only 1 to 3 numbers')

    print(f"Player choice is : {Player_1}\nComputers choice is : {Computer}")    
    print(check(Player_1,Computer))
# resulting the game scenarios to the users !
print(f'\nThe Game Scenarios are...\n{j}\n')
print(f"Player wins = {Won}\nPlayer Loses = {Loss}\nMatch ties = {Tie}" )

# End of the Project !!!