'''
BlackJack.py

Rules
    - Dealer stands on ALL 17's
    - Can re-split aces

As part of the Blackjack suite
@author Oneal Abdulrahim
'''
from Card import CARD_SYMBOLS
from Deck import Deck
from Hand import Hand
import time


DEALER_HAND = Hand([],0)
PLAYER_HANDS = [Hand([],0)]


def cleanup_table():
    print("[DBG] FUNC ENTRY: cleanup_table")
    DEALER_HAND.clear_hand()
    for hand in PLAYER_HANDS:
        hand.clear_hand()
    while (len(PLAYER_HANDS) > 1):
        PLAYER_HANDS.pop(0)

# create and shuffle deck
def create_shuffle_deck(number_of_decks):
    print("[DBG] FUNC ENTRY: create_shuffle_deck")
    deck = Deck(number_of_decks)
    deck.shuffle_deck()
    return deck
    
# Burn a card, return burned card
def burn_card(deck):
    print("[DBG] FUNC ENTRY: burn_card")
    burned_card = deck.pop_card().get_card_symbol()
    return burned_card

def initial_draw(deck):
    cleanup_table()
    print("[DBG] FUNC ENTRY: draw")
    PLAYER_HANDS[0].add_card(deck.pop_card())
    DEALER_HAND.add_card(deck.pop_card())
    PLAYER_HANDS[0].add_card(deck.pop_card())
    DEALER_HAND.add_card(deck.pop_card())

def surrender(hand):
    print("\nplayer surrendered hand")
    hand.clear_hand()
    hand.stand = True

def stand(hand):
    print("\nplayer stands")
    hand.stand = True

def hit(hand, deck):
    print("\n\n\n\n\n\n\n\n\n\nplayer hits")
    hand.add_card(deck.pop_card())

def double(hand, deck):
    print("\n\n\n\n\n\n\n\n\n\nplayer doubles")
    hand.add_card(deck.pop_card())
    hand.stand = True

def split(hand, deck):
    print("\nplayer splits")
    
    new_hand = Hand([hand.cards[1]])
    hand.remove_last_card()

    # only one more card with split aces
    if hand.cards[0].rank == "Ace":
        new_hand.add_card(deck.pop_card())
        new_hand.stand = True
        PLAYER_HANDS.append(new_hand)
        hand.add_card(deck.pop_card())
        hand.stand
    else:
        PLAYER_HANDS.append(new_hand)

def check_blackjack():
    print("[DBG] FUNC ENTRY: player_loop")

    # Does dealer have BlackJack?
    if DEALER_HAND.count == 21:
        if PLAYER_HANDS[0].count != 21:
            print("\nDealer has BlackJack!")
            return(-1)
        else:
            print("push.... BlackJack = BlackJack")
            return(0)
    # Does the player have BlackJack?
    elif PLAYER_HANDS[0].count == 21: 
        print("\nplayer has BlackJack!")
        return(1)

def dealer_draw(deck):
    print("[DBG] FUNC ENTRY: dealer_loop")
    DEALER_HAND.add_card(deck.pop_card())