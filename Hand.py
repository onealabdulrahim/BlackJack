'''
Hand.py
Contains the playing Hand class and helper functions to track a hand.
As part of the Blackjack suite
@author Oneal Abdulrahim
'''

class Hand:

    def __init__(self, cards=[], count=0, stand=False):
        self.cards = cards
        self.count = count
        self.stand = False

        self.update_count()

    def __str__(self):
        for card in self.cards:
            print(card.get_card_symbol(), end=' ')
        return '\n  {self.count}'.format(self=self)

    def update_count(self):
        # prevent double-counting
        self.count = 0
        # the set is not ordered. so, a first pass of non-aces must be calculated
        # then, we know if we need to treat the aces as 1 or 11
        ace_count = 0
        for card in self.cards:
            if card.value != 1:
                self.count += card.value
            else:
                ace_count += 1
        # aces only "help" the count
        for _ in range(0, ace_count):
            if self.count + 11 <= 21:
                self.count += 11
            else:
                self.count += 1
            
    def add_card(self, card):
        # add card
        self.cards.append(card)
        # update count
        self.update_count()

    # for use with splits
    def remove_last_card(self):
        self.cards.pop(0)
        self.update_count()

    def clear_hand(self):
        self.cards.clear()
        self.count = 0
        self.stand = False
          