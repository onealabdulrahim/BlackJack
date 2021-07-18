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
    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value

    def __str__(self):
        return '{self.rank} of {self.suit}'.format(self=self)

    def get_card_symbol(self):
        if self.rank == "Jack":
            return CARD_SYMBOLS[self.suit.value * 13 + 11]
        elif self.rank == "Queen":
            return CARD_SYMBOLS[self.suit.value * 13 + 12]
        elif self.rank == "King":
            return CARD_SYMBOLS[self.suit.value * 13 + 13]
        return CARD_SYMBOLS[self.suit.value * 13 + self.value]
        