
from random import randint

def chooseTypeOfQuestion():
    return randint(1,5)

if __name__ == '__main__':
    while(true):
        type = chooseTypeOfQuestion()
        playRound(type)
