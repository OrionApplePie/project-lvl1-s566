import operator
import random
from ..cli import game_flow, MAX_NUMBER


RULES = 'What is the result of the expression?\n'


def question_generator():
    ops = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul
    }
    number1 = random.randint(0, MAX_NUMBER)
    number2 = random.randint(0, MAX_NUMBER)

    op = random.choice(list(ops.keys()))
    expr = '{0} {1} {2}'.format(number1, op, number2)
    question = 'Question: {0}'.format(expr)

    correct_answer = str(ops[op](number1, number2))

    return {
        'question': question,
        'answer': correct_answer
    }


game = game_flow(RULES, question_generator)
