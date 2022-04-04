from Questions_Answers.Movies import questions_movies
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
