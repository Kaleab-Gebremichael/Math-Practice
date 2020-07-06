
from random import choice
from random import randint

DEFAULT_NUM_OF_QUESTIONS = 10

QUESTION_TYPES = ['+', '-', '*', '/', '√']
OPERATIONS = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x // y,
    '√': lambda x: sqrt(x)
}

def chooseTypeOfQuestion():
    return choice(QUESTION_TYPES)

def playRound(typeOfQuestion):
    firstNum = randint(1,100)
    secondNum = randint(1,100)
    print(firstNum, " ", typeOfQuestion, " ", secondNum)
    userAnswer = input()
    rightAnswer = OPERATIONS[typeOfQuestion](firstNum, secondNum)
    return userAnswer == rightAnswer


if __name__ == '__main__':
    score = 0
    for i in range(DEFAULT_NUM_OF_QUESTIONS):
        typeOfQuestion = chooseTypeOfQuestion()
        correct = playRound(typeOfQuestion)
        if (correct):
            score += 1

    print("Your final score is ", score)
