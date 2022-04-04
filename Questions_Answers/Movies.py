from Questions_Answers.Countries import questions_on_countries

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
