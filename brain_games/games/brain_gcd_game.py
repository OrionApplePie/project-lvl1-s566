import random
from brain_games.engine import MAX_NUMBER


RULES = 'Find the greatest common divisor of given numbers.'


def gcd(x, y):
    while(y):
        x, y = y, x % y
    return x


def get_round():
    number1 = random.randint(0, MAX_NUMBER)
    number2 = random.randint(0, MAX_NUMBER)

    question = '{0} {1}'.format(number1, number2)
    correct_answer = str(gcd(number1, number2))

    return question, correct_answer
