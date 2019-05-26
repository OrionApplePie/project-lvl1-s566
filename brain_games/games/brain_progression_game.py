import random
from ..cli import game_flow, MAX_PROGRESSION_NUMBERS


RULES = 'What number is missing in the progression?.\n'


def question_generator():
    start = random.randint(0, MAX_PROGRESSION_NUMBERS)
    step = random.randint(1, MAX_PROGRESSION_NUMBERS)
    end = start + step * MAX_PROGRESSION_NUMBERS

    hidden_number_index = random.randint(0, MAX_PROGRESSION_NUMBERS - 1)

    progression = list(range(start, end, step))
    correct_answer = str(progression[hidden_number_index])
    progression[hidden_number_index] = '..'

    progression_string = ' '.join(map(str, progression))
    question = 'Question: {0}'.format(progression_string)

    return {
        'question': question,
        'answer': correct_answer
    }


game = game_flow(RULES, question_generator)
