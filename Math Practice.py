
from random import choice

QUESTION_TYPES = ['+', '-', '*', '/', '√']
DEFAULT_NUM_OF_QUESTIONS = 10

def chooseTypeOfQuestion():
    return choice(QUESTION_TYPES)

def playRound(typeOfQuestion):
    print(typeOfQuestion)


if __name__ == '__main__':
    for i in range(DEFAULT_NUM_OF_QUESTIONS):
        typeOfQuestion = chooseTypeOfQuestion()
        playRound(typeOfQuestion)
