"""
Write a method to shuffle a deck of cards. It must be a perfect shuffle -
in other words, each of the 52! permutations of the deck has to be equally
likely. Assume you are given a random number generator which is perfect.
"""

import random

card_deck = []
for i in range(0, 52):
    card_deck.append(i)


def shuffle():
    """
    move through the array and for each element i, swap array[i]
    with a random element between 0 and i, inclusive
    """
    for i in range(1, len(card_deck)):
        to_be_swapped = random.randint(0, i)
        card_deck[i], card_deck[to_be_swapped] = card_deck[to_be_swapped], card_deck[i]

    return card_deck


print(shuffle())
