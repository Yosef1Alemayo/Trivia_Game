
def questions_on_sport():
    counter = 0
    print('\nSection 1: Sport')
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
    print('----------------------------')
    print('\nScore :', counter, 'Points')
    print('\n----------------------------')
    return counter


def questions_on_countries():
    new_counter = questions_on_sport()
    print('\n\n\nSection 2: Countries')
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

    print('\n\nQuestion5 - What is the capital of Portugal ?')
    print('1. Amadora\n2. Braga\n3. Lisbon\n4. Porto')
    ans1 = int(input('Your Answer: '))
    while ans1 not in range(1, 5):
        ans1 = int(input('Wrong Number , Try Again: '))
    if ans1 == 3:
        new_counter += 10
        print('Correct Answer ☻ ')
    else:
        print('Incorrect Answer ! ')

    print("\n\nQuestion6 - What is The Capital of Kenya ?")
    print('1. Nairobi\n2. Eldoret\n3. Mombasa \n4. Nakuru')
    ans1 = int(input('Your Answer: '))
    while ans1 not in range(1, 5):
        ans1 = int(input('Wrong Number , Try Again: '))
    if ans1 == 1:
        new_counter += 10
        print('Correct Answer ☻ ')
    else:
        print('Incorrect Answer ! ')
    print('-----------------------------')
    print('\nScore :', new_counter, 'Points')
    print('\n---------------------------')
    return new_counter

def questions_movies():
    new_counter1 = questions_on_countries()
    print('\n\nSection 3: Movies')
    print("\nQuestion7 - ' When did the first Harry Potter film come out ?")
    print('1. 2002\n2. 1997\n3. 2001\n4. 1999')
    answer = int(input('Your Answer:'))
    while answer not in range(1, 5):
        answer = int(input('Wrong Number, Try Again:'))
    if answer == 3:
        new_counter1 += 10
        print("Correct Answer")
    else:
        print("Incorrect Answer")

    print('\n\nQuestion8 -How many seasons does the paper house have ?')
    print('1. 4\n2. 6\n3. 3\n4. 5')
    ans1 = int(input('Your Answer: '))
    while ans1 not in range(1, 5):
        ans1 = int(input('Wrong Number , Try Again: '))
    if ans1 == 4:
        new_counter1 += 10
        print('Correct Answer ☻ ')
    else:
        print('Incorrect Answer ! ')

    print("\n\nQuestion9 - What is the most profitable film in history ?")
    print('1. Supermen\n2. the Avengers\n3. The train \n4. Harry Potter')
    ans1 = int(input('Your Answer: '))
    while ans1 not in range(1, 5):
        ans1 = int(input('Wrong Number , Try Again: '))
    if ans1 == 2:
        new_counter1 += 10
        print('Correct Answer ☻ ')
    else:
        print('Incorrect Answer ! ')
    print('-----------------------------------')
    print('\nScore: ', new_counter1, 'Points')
    print('\n----------------------------------')
    return new_counter1


def bonus_question():
    new_counter2 = questions_movies()
    print("\n\nQuestion10 - If we want even numbers what should we use?")
    print('1. == \n2. % 2\n3. 2 %\n4. ! = ')
    ans1 = int(input('Your Answer: '))
    while ans1 not in range(1, 5):
        ans1 = int(input('Wrong Number , Try Again: '))
    if ans1 == 2:
        new_counter2 += 20
        print('Correct Answer ☻ ')
    else:
        print('Incorrect Answer ! ')
    print('----------------------------------------')
    print('\n Total Score: ', new_counter2, 'Points')
    print('\n----------------------------------------')
    return new_counter2

# How To Combine The Functions:
