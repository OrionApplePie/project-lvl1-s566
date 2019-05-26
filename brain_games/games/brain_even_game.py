import prompt
import random



GAME_ROUNDS = 3
MAX_NUMBER = 100


def print_rules():
    rules = 'Answer "yes" if number even otherwise answer "no".\n'
    print(rules)


def game(name):
    score = 0

    for round in range(GAME_ROUNDS):
        number = random.randint(0, MAX_NUMBER)
        correct_answer = 'yes' if number % 2 == 0 else 'no'

        print('Question: {0}'.format(number))
        answer = prompt.string('Your answer: ')
        
        if answer == correct_answer:
            print('Correct!')
            score += 1
        else:
            print("'{0}' is wrong answer ;(. Correct answer was '{1}'.".format(answer, correct_answer))
            print("Let's try again, {0}!".format(name))
            break
    
    if score == GAME_ROUNDS:
        print('Congratulations, {0}!'.format(name))
