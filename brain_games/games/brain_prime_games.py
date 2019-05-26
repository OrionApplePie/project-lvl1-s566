import random
from ..cli import game_flow, MAX_NUMBER_FOR_PRIMES


RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".\n'


def is_prime(n):
    for num in range(2, int(n ** 0.5) + 1):
        if n % num == 0:
            return False
    return True


def question_generator():
    number = random.randint(2, MAX_NUMBER_FOR_PRIMES)
    question = 'Question: {0}'.format(number)
    correct_answer = 'yes' if is_prime(number) else 'no'

    return {
        'question': question,
        'answer': correct_answer
    }


game = game_flow(RULES, question_generator)
