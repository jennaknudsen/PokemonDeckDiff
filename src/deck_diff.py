from deck import Deck
from sys import argv
from os import system

def deck_diff(deck_file_1, deck_file_2):
    deck_1 = Deck(deck_file_1)
    deck_2 = Deck(deck_file_2)
    print(deck_1.diff(deck_2))


if __name__ == '__main__':
    system('color') # gets terminal colors working on Windows
    if len(argv) < 3:
        raise RuntimeError('Program must be run with two decklists separated by spaces')
    deck_diff(argv[1], argv[2])