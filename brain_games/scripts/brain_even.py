from ..games.brain_even_game import print_rules, game
from ..cli import run


def main():
    print("Welcome to the Brain Games!")
    print_rules()
    name = run()
    game(name)


if __name__ == "__main__":
    main()
