'''
Card.py
Contains the Card class and helper functions to determine card information
As part of the Blackjack suite
@author Oneal Abdulrahim
'''

CARD_SYMBOLS = ["🂠", "🃑","🃒","🃓","🃔","🃕","🃖","🃗","🃘","🃙","🃚","🃛","🃝","🃞",
                     "🃁","🃂","🃃","🃄","🃅","🃆","🃇","🃈","🃉","🃊","🃋","🃍","🃎",
                     "🂱","🂲","🂳","🂴","🂵","🂶","🂷","🂸","🂹","🂺","🂻","🂽","🂾",
                     "🂡","🂢","🂣","🂤","🂥","🂦","🂧","🂨","🂩","🂪","🂫","🂭","🂮"]

class Card:
    def __init__(self, suit, rank, value, symbol):
        self.suit = suit
        self.rank = rank
        self.value = value
        self.symbol = symbol

    def __str__(self):
        return '{self.rank} of {self.suit}'.format(self=self)

    def get_card_symbol(self):
        return self.symbol
        