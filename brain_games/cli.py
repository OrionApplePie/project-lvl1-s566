import prompt


ROUNDS_COUNT = 3
MAX_NUMBER = 100
PROGRESSION_NUMBERS_COUNT = 10
NUMBERS_FOR_PRIMES_COUNT = 5000


def conversation(rules=None):
    """Функция приветствия, печатает правила игры и возвращает имя игрока."""
    print("Welcome to the Brain Games!")
    if rules:
        print(rules)
    else:
        print('\n')
    user_name = prompt.string('May I have your name? ')
    print('Hello, {0}!\n'.format(user_name))
    return user_name


def game_flow(rules, question_generator):
    """Общеигровой флоу."""
    def game():
        user_name = conversation(rules)
        score = 0
        for _ in range(ROUNDS_COUNT):
            question, correct_answer = question_generator().values()
            print('Question: {0}'.format(question))
            user_answer = prompt.string('Your answer: ')
            if user_answer == correct_answer:
                print('Correct!')
                score += 1
            else:
                print(
                    ("'{0}' is wrong answer ;(."
                     "Correct answer was '{1}'.".format(
                         user_answer, correct_answer))
                )
                print("Let's try again, {0}!".format(user_name))
                break

        if score == ROUNDS_COUNT:
            print('Congratulations, {0}!'.format(user_name))
    return game
