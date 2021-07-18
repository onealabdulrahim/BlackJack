#DEPRECATED

'''
CardStack.py
A "CardStack" is a collection of standard card decks.
It offers helper functions to pull a card and shuffle.

Table games involving one or multiple decks of cards involve
stacked card decks, and are shuffled as a complete "CardStack"
instead of each deck individually.

As part of the Blackjack suite
@author Oneal Abdulrahim
'''

from Deck import Deck

class CardStack:

    # start with standard 52 cards per deck
    def __init__(self, num_decks, cards=[]):
        self.num_decks = num_decks
        self.cards = cards

        for x in range(0, self.num_decks):
            self.cards.append(Deck(x))

    def __str__(self):
        return 