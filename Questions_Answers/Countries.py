from Questions_Answers.Sports import questions_on_sport

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
