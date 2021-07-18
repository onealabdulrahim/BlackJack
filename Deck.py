'''
Deck.py
Contains the Deck class and helper functions to track deck information.
It offers helper functions to pull a card and shuffle.

A "CardStack" is a collection of standard-count (52) card decks.

Table games involving one or multiple decks of cards involve
stacked card decks, and are shuffled as a complete "CardStack"
instead of each deck individually.

As part of the Blackjack suite
@author Oneal Abdulrahim
'''

from Card import Card
from Suit import *
from random import shuffle

RANKS_VALUES = (("Ace", 1), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), ("Jack", 10), ("Queen", 10), ("King", 10))
SUITS = [Suit("Clubs", "♣", 0), Suit("Diamonds", "♦", 1), Suit("Hearts", "♥", 2), Suit("Spades", "♠", 3)]

class Deck:
    def __init__(self, num_decks, cards=[]):
        self.cards = cards
        if num_decks > 0:
            self.num_decks = num_decks
        else:
            self.num_decks = 1

        for _ in range(0, num_decks):
            for suit in SUITS:
                for ranks_values in RANKS_VALUES:
                    self.cards.append(Card(suit, ranks_values[0], ranks_values[1]))

    def __str__(self):
        for card in self.cards:
            print(card)
        return ""

    def shuffle_deck(self):
        shuffle(self.cards)

    def pop_card(self):
        if (len(self.cards) > 0):
            return self.cards.pop(0)
