import operator
import random
from brain_games.engine import MAX_NUMBER


RULES = 'What is the result of the expression?'
OPERATIONS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul
}


def get_round():
    number1 = random.randint(0, MAX_NUMBER)
    number2 = random.randint(0, MAX_NUMBER)

    op = random.choice(list(OPERATIONS.keys()))

    question = '{0} {1} {2}'.format(number1, op, number2)
    correct_answer = str(OPERATIONS[op](number1, number2))

    return question, correct_answer
