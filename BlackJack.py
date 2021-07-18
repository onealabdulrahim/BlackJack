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

NUMBER_OF_DECKS = 6
CUT_CARD_COUNT = 10
DECK = Deck(6)

# Dealer Hand
DEALER_HAND = Hand([],0)
# Player Hands
PLAYER_HANDS = [Hand([],0)]


def cleanup_table():
    #DEALER_HAND.clear_hand()
    #for hand in PLAYER_HANDS:
    #    hand.clear_hand()
    #while (len(PLAYER_HANDS) > 1):
    #    PLAYER_HANDS.pop(0)
    #initial_draw()
    exit()

def show_cards_hidden_dealer():
    # show some cards
    print("\n\n\n\n\n\n\n\n\n\n\nDEALER\n", DEALER_HAND.cards[0].get_card_symbol(), CARD_SYMBOLS[0])
    print(DEALER_HAND.count - DEALER_HAND.cards[1].value)
    for hand in PLAYER_HANDS:
        print("\nPLAYER\n", hand)

def show_cards_flipped_dealer():
    # show all cards
    print("\n\n\n\n\n\n\n\n\n\n\nDEALER\n", DEALER_HAND)
    for hand in PLAYER_HANDS:
        print("\nPLAYER\n", hand)

def initial_draw():
    # Player, dealer, player, dealer, yes it matters
    PLAYER_HANDS[0].add_card(DECK.pop_card())
    DEALER_HAND.add_card(DECK.pop_card())
    PLAYER_HANDS[0].add_card(DECK.pop_card())
    DEALER_HAND.add_card(DECK.pop_card())

    # Does dealer have BlackJack?
    if DEALER_HAND.count == 21:
        if PLAYER_HANDS[0].count != 21:
            print("\nDealer has BlackJack!")
        else:
            print("push")
        show_cards_flipped_dealer()
        cleanup_table()
    # Does the player have BlackJack?
    elif PLAYER_HANDS[0].count == 21: 
        print("\nplayer has BlackJack!")
        cleanup_table()

def player_loop():
    # Player has some options
    for hand in PLAYER_HANDS:
        while not hand.stand:
            show_cards_hidden_dealer()
            print("\n0: surrender\n1: stand\n2: hit\n3: double")
            # if matching card value pair, split is available. note you can only split IFF 2 cards in a hand
            if len(hand.cards) == 2:
                if PLAYER_HANDS[0].cards[0].value == PLAYER_HANDS[0].cards[1].value:
                    print("4: split")
            player_choice = (input("\naction: "))

            if player_choice == "0":
                print("\nplayer surrendered hand")
                hand.clear_hand()
                hand.stand = True
            elif player_choice == "1":
                print("\nplayer stands")
                hand.stand = True
            elif player_choice == "2":
                print("\n\n\n\n\n\n\n\n\n\nplayer hits")
                hand.add_card(DECK.pop_card())
                if hand.count > 21:
                    show_cards_flipped_dealer()
                    print("\n\nbust!")
                    time.sleep(2)
                    cleanup_table()
                else:
                    show_cards_hidden_dealer()
            elif player_choice == "3":
                print("\n\n\n\n\n\n\n\n\n\nplayer doubles")
                hand.add_card(DECK.pop_card())
                show_cards_hidden_dealer()
                hand.stand = True
            elif player_choice == "4":
                print("\nplayer splits")
                
                new_hand = Hand([hand.cards[1]])
                hand.remove_last_card()

                # only one more card with split aces
                if hand.cards[0].rank == "Ace":
                    new_hand.add_card(DECK.pop_card())
                    new_hand.stand = True
                    PLAYER_HANDS.append(new_hand)
                    hand.add_card(DECK.pop_card())
                    hand.stand
                else:
                    PLAYER_HANDS.append(new_hand)
                

def dealer_loop():
    show_cards_flipped_dealer()
    time.sleep(1)

    while DEALER_HAND.count < 17:
        DEALER_HAND.add_card(DECK.pop_card())
        show_cards_flipped_dealer()
        time.sleep(1)

    if DEALER_HAND.count > 21:
        print("dealer bust")
    else:
        for hand in PLAYER_HANDS:
            if DEALER_HAND.count > hand.count:
                print("dealer win")
            else:
                print("player win")
            print("{} > {}".format(DEALER_HAND.count, hand.count))
    cleanup_table()

# Shuffle Deck
DECK.shuffle_deck()

# Burn a card, show burn
print('\nburn card:', DECK.pop_card().get_card_symbol())

initial_draw()
player_loop()
dealer_loop()