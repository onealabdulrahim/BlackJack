'''
Suit.py
Contains the Suit class and helper functions to carry card suit information
As part of the Blackjack suite
@author Oneal Abdulrahim
'''

class Suit:
    def __init__(self, suit, symbol, value):
        self.suit = suit
        self.symbol = symbol
        self.value = value

    def __str__(self):
        return '{self.symbol}{self.suit}{self.symbol}'.format(self=self)