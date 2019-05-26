import random
from ..cli import game_flow, MAX_PROGRESSION_NUMBER


RULES = 'What number is missing in the progression?.\n'


def question_generator():
    start = random.randint(0, MAX_PROGRESSION_NUMBER)
    step = random.randint(1, MAX_PROGRESSION_NUMBER)
    end = start + step * MAX_PROGRESSION_NUMBER

    hidden_number_index = random.randint(1, MAX_PROGRESSION_NUMBER)

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
