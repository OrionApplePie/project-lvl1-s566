import random
from brain_games.engine import PROGRESSION_NUMBERS_COUNT


RULES = 'What number is missing in the progression?.'


def get_round():
    start = random.randint(0, PROGRESSION_NUMBERS_COUNT)
    step = random.randint(1, PROGRESSION_NUMBERS_COUNT)
    end = start + step * PROGRESSION_NUMBERS_COUNT

    progression = list(range(start, end, step))
    hidden_number_index = random.randint(0, PROGRESSION_NUMBERS_COUNT - 1)
    correct_answer = str(progression[hidden_number_index])

    progression[hidden_number_index] = '..'
    question = ' '.join(map(str, progression))

    return question, correct_answer
