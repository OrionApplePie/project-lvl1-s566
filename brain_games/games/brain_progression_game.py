import random
from brain_games.cli import game_flow, PROGRESSION_NUMBERS_COUNT


RULES = 'What number is missing in the progression?.\n'


def question_generator():
    start = random.randint(0, PROGRESSION_NUMBERS_COUNT)
    step = random.randint(1, PROGRESSION_NUMBERS_COUNT)
    end = start + step * PROGRESSION_NUMBERS_COUNT

    progression = list(range(start, end, step))
    hidden_number_index = random.randint(0, PROGRESSION_NUMBERS_COUNT - 1)
    correct_answer = str(progression[hidden_number_index])

    progression[hidden_number_index] = '..'
    question = ' '.join(map(str, progression))
    return {
        'question': question,
        'answer': correct_answer
    }


game = game_flow(RULES, question_generator)
