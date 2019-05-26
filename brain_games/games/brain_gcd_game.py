import random
from ..cli import game_flow, MAX_NUMBER


RULES = 'Find the greatest common divisor of given numbers.\n'


def GCD(x, y): 
    while(y):
        x, y = y, x % y 
    return x 


def question_generator():
    number1 = random.randint(0, MAX_NUMBER)
    number2 = random.randint(0, MAX_NUMBER)

    question = 'Question: {0} {1}'.format(number1, number2)
    correct_answer = str(GCD(number1, number2))

    return {
        'question': question,
        'answer': correct_answer
    }


game = game_flow(RULES, question_generator)
