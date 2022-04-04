from Questions_Answers.Bonus_Question import bonus_question
def start_the_game():
    print('---------------------------------------------------------')
    print('Welcome To Trivia Game ☻\nThere is 9 Questions and One is Bonus!')
    print('---------------------------------------------------------')
    start = int(input('To Start Play Press 1:\nTo Exit Press 2 :'))
    while (start != 1) and (start != 2):
        start = int(input('Try Again:'))
        if start == 2:
            print('GoodBye')
            break
    if start == 1:
        user = input('Enter NickName:')
        print('--------------------------')
        print('Good Luck' + ' '+user)
        print('------------------------')
        st = bonus_question()
        if st >= 100:
            print(user, 'You The Best ! ')
        else:
            print(user, 'You can do better than that')
        return st

