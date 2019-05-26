import prompt


def run():
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!\n'.format(name))
    return name
