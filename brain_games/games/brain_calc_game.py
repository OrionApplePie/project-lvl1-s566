import operator
import prompt
import random


GAME_ROUNDS = 3
MAX_NUMBER = 100


def print_rules():
    rules = 'What is the result of the expression?\n'
    print(rules)


def game(name):
    ops = {
        '+': operator.add,
        '-': operator.sub, 
        '*': operator.mul
    }
    score = 0

    for round in range(GAME_ROUNDS):
        number1 = random.randint(0, MAX_NUMBER)
        number2 = random.randint(0, MAX_NUMBER)
        op = random.choice(list(ops.keys()))

        expr = '{0} {1} {2}'.format(number1, op, number2)

        correct_answer = str(ops[op](number1, number2))

        print('Question: {0}'.format(expr))

        answer = prompt.string('Your answer: ')

        if answer == correct_answer:
            print('Correct!')
            score += 1
        else:
            print(
                ("'{0}' is wrong answer ;(."
                 "Correct answer was '{1}'.".format(answer, correct_answer))
            )
            print("Let's try again, {0}!".format(name))
            break
    if score == GAME_ROUNDS:
        print('Congratulations, {0}!'.format(name))
