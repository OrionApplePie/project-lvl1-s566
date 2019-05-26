#!/usr/bin/env python3
from ..games.brain_calc_game import print_rules, game
from ..cli import run


def main():
    print("Welcome to the Brain Games!")
    print_rules()
    name = run()
    game(name)


if __name__ == "__main__":
    main()
