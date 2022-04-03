

def questions_Country():
    counter = 0
    print("question4 :' what is capital city of israel?")
    print('1. Haifa\n2. Paris\n3. Tel-Aviv\n4. Jerusalem')
    answer = int(input('Answer:'))
    while answer not in range(1,5):
        answer = int(input('try again:'))
    if answer ==4:
        print("correct answer")
    else:
        print("incorrect answer")


def questions_largest():
    counter = 0
    print('question5 : What is the largest island in the world?')
    print('1. grinlend\n2. honsho\n3. janna\n4. madgaster')
    answer = int(input('Answer:'))
    while answer not in range(1,5):
        answer = int(input('try again:'))
    if answer ==1:
        print("correct answer")
    else:
        print("incorrect answer")



def question_beer():
    counter = 0
    print('question6 : Which beer is produced in the Netherlands?')
    print('1. maccabi\n2. heineken\n3. corona\n4. tuborg')
    answer = int(input('Answer:'))
    while answer not in range(1,5):
        answer = int(input('try again:'))
    if answer ==2:
        print("correct answer")
    else:
        print("incorrect answer")



questions_Country()
questions_largest()
question_beer()