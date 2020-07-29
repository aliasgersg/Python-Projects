# Rock Paper Scissors Game

from random import randint
from time import sleep

print('-'*10, 'The Game', '-'*10)
playerName = input("Enter your name")
print(playerName, "V/S AI")

options = ['Rock', 'Paper', 'Scissors']

exitGame = False

validChoices = ['1', '2', '3', '4']
while not exitGame:
    sleep(1)
    print('\n', '1. Rock', '2. Paper', '3. Scissors', '4. Quit', sep = '\n')
    playerChoice = input("Enter your number: ")
    AIchoice = options[randint(0,2)]
    if playerChoice in validChoices:
        ''' Giving Winning Choices '''

        # if player chose ROCK
        if playerChoice == '1':
            if AIchoice == 'Paper':
                print("AI Wins, YOU LOSE!", sep = '\n')
            elif AIchoice == 'Rock':
                print("AI and YOU DRAW!", sep = '\n')
            else:
                print('AI', AIchoice)
                print('YOU WIN!')
        # if player chose PAPER
        elif playerChoice == '2':
            if AIchoice == 'Scissor':
                print("AI Wins, YOU LOSE!", sep = '\n')
            elif AIchoice == 'Paper':
                print("AI and YOU DRAW!", sep = '\n')
            else:
                print('AI', AIchoice)
                print('YOU WIN!')
        # if player chose SCISSOR
        elif playerChoice == '3':
            if AIchoice == 'Rock':
                print("AI Wins, YOU LOSE!", sep = '\n')
            elif AIchoice == 'Scissor':
                print("AI and YOU DRAW!", sep = '\n')
            else:
                print('AI', AIchoice)
                print('YOU WIN!')
        # 4 Means EXIT
        else:
            print('\n Thanks for playing :)')
            exitGame = True
    else:
        print('%'*10, 'ERROR, Please enter within range (1-4)', '%'*10)







