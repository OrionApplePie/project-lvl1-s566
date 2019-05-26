import random
from ..cli import game_flow, MAX_NUMBER


RULES = 'Answer "yes" if number even otherwise answer "no".\n'


def question_generator():
    number = random.randint(0, MAX_NUMBER)
    correct_answer = 'yes' if number % 2 == 0 else 'no'
    return {
        'question': str(number),
        'answer': correct_answer
    }


game = game_flow(RULES, question_generator)
