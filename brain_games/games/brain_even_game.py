import random
from brain_games.engine import MAX_NUMBER


RULES = 'Answer "yes" if number even otherwise answer "no".'


def get_round():
    number = random.randint(0, MAX_NUMBER)

    question = str(number)
    correct_answer = 'yes' if number % 2 == 0 else 'no'

    return question, correct_answer
