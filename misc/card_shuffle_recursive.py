"""
Write a method to shuffle a deck of cards. It must be a perfect shuffle -
in other words, each of the 52! permutations of the deck has to be equally
likely. Assume you are given a random number generator which is perfect.
"""

import random

card_deck = [j for j in range(0, 52)]

def shuffle(card_deck, i):
    """
    Recursively move through the array and for each element i, swap array[i]
    with a random element between 0 and i, inclusive
    """
    if i == 0:
        return card_deck

    shuffle(card_deck, i-1)

    # generate random number between 0 and i inclusive
    to_be_swapped = random.randint(0, i)
    card_deck[i], card_deck[to_be_swapped] = card_deck[to_be_swapped], card_deck[i]

    return card_deck

print shuffle(card_deck, len(card_deck)-1)


