import random
from brain_games.engine import NUMBERS_FOR_PRIMES_COUNT


RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(n):
    for num in range(2, int(n ** 0.5) + 1):
        if n % num == 0:
            return False
    return True


def get_round():
    number = random.randint(2, NUMBERS_FOR_PRIMES_COUNT)

    question = str(number)
    correct_answer = 'yes' if is_prime(number) else 'no'

    return question, correct_answer
