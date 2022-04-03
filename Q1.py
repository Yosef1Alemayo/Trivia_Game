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

def questions_Country():
    new_counter= questions_on_sport()
    print('\n\nSection 3: Countries')
    print("question7 :' what is capital city of israel?")
    print('1. Haifa\n2. Paris\n3. Tel-Aviv\n4. Jerusalem')
    answer = int(input('Answer:'))
    while answer not in range(1,5):
        answer = int(input('try again:'))
    if answer ==4:
        new_counter =+ 10
        print("correct answer")
    else:
        print("incorrect answer")
    print('points:', new_counter)


    print('question8 : What is the largest island in the world?')
    print('1. grinlend\n2. honsho\n3. janna\n4. madgaster')
    answer = int(input('Answer:'))
    while answer not in range(1,5):
        answer = int(input('try again:'))
    if answer ==1:
        new_counter=+10
        print("correct answer")
    else:
        print("incorrect answer")
    print('points:',new_counter)


    new_counter=
    print('question9 : Which beer is produced in the Netherlands?')
    print('1. maccabi\n2. heineken\n3. corona\n4. tuborg')
    answer = int(input('Answer:'))
    while answer not in range(1,5):
        answer = int(input('try again:'))
    if answer ==2:
        new_counter =+10
        print("correct answer")
    else:
        print("incorrect answer")
        return new_counter
