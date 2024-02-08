import random
rock, paper, scissor = 0 , 1, 2
user=input("Choose Rock, Paper and Scissors: ")
user_choice= 0 if user.upper()=='ROCK' else 1 if user.upper()=='PAPER' else 2 if user.upper()=='SCISSOR' else 3
com_choice=random.randint(0,2)
if user_choice==3:
    print('You have entered invalid choice, Computer Wins')
elif user_choice==com_choice:
    print('Draw')
elif user_choice==0:
    if com_choice==1:
        print('Computer chooses Paper and wins, You Lose')
    else:
        print('Computer chooses Scissors and loses, You win')
elif user_choice==1:
    if com_choice==0:
        print('Computer chooses Rock and loses, You win')
    else:
        print('Computer chooses Scissors and wins, You lose')
else:
    if com_choice==0:
        print('Computer chooses Rock and wins, You lose')
    else:
        print('Computer chooses Paper and loses, You win')