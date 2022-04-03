def start_game():
    print('-----Welcome To Trivia Game ☻-----\n-----There is 9 Questions and One is Bonus!-----')
    start = int(input('To Start Press 1, Press 2 To Exit: '))
    while start != 1:
        start = int(input('Wrong Number, Press 1 Or 2:'))
        if start == 2:
            print('GoodBye !')
            break


def questions_on_sport():
    counter = 0
    print('Section 1: Sport')
    print('\nQuestion1 - Who was the first player to score at five World Cup editions ?')
    print('1. Marta\n2. Pele\n3. Ronaldo\n4. Lionel Messi')
    ans1 = int(input('Your Answer: '))
    while ans1 not in range(1, 5):
        ans1 = int(input('Wrong Number , Try Again: '))
    if ans1 == 1:
        counter += 10
        print('Correct Answer ☻ ')
    else:
        print('Incorrect Answer ! ')

    print("\n\nQuestion2 - Who was the first English player to win league titles in four countries'?")
    print('1. Jimmy Greaves\n2. Peter Shilton\n3. David Beckham \n4. Asaf Avrham')
    ans1 = int(input('Your Answer: '))
    while ans1 not in range(1, 5):
        ans1 = int(input('Wrong Number , Try Again: '))
    if ans1 == 3:
        counter += 10
        print('Correct Answer ☻ ')
    else:
        print('Incorrect Answer ! ')

    print("\n\nQuestion3 - Who has the Most Champions Leauge Titles ?")
    print('1. Liverpool\n2. Barcelona\n3. Ajax \n4. Real-Madrid')
    ans1 = int(input('Your Answer: '))
    while ans1 not in range(1, 5):
        ans1 = int(input('Wrong Number , Try Again: '))
    if ans1 == 4:
        counter += 10
        print('Correct Answer ☻ ')
    else:
        print('Incorrect Answer ! ')
    print('Section1 -- Your Points:', counter)
    return counter

def questions_on_countries():
    new_counter = questions_on_sport()
    print('\n\nSection 2: Countries')
    print('\nQuestion4 - What is the capital of United States of America ?')
    print('1. Seattle\n2. Washington D.C.\n3. Chicago\n4. New York')
    ans1 = int(input('Your Answer: '))
    while ans1 not in range(1, 5):
        ans1 = int(input('Wrong Number , Try Again: '))
    if ans1 == 2:
        new_counter += 10
        print('Correct Answer ☻ ')
    else:
        print('Incorrect Answer ! ')

    print('points:', new_counter)

questions_on_countries()