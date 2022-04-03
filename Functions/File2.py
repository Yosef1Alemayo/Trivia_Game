from Questions_Answers.File1 import *
def start_game():
    print('-----Welcome To Trivia Game ☻-----\n-----There is 9 Questions and One is Bonus!-----')
    start = int(input('To Start Press 1, Press 2 To Exit: '))
    while start not in range(1, 3):
        start = int(input('Wrong Number, Press 1 Or 2:'))
        if start == 2:
            print('GoodBye !')
            break


