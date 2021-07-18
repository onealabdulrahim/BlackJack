'''
BlackJack.py

Rules
    - Dealer stands on ALL 17's
    - Can re-split aces

As part of the Blackjack suite
@author Oneal Abdulrahim
'''
from tkinter.constants import ACTIVE, DISABLED, HIDDEN
from Card import CARD_SYMBOLS
from Deck import Deck
from Hand import Hand
import time
import tkinter

NUMBER_OF_DECKS = 1
CUT_CARD_COUNT = 8
PLAYER_WINS = 0
DEALER_WINS = 0
TOTAL_HANDS = 0
DECK = Deck(0)
DEALER_HAND = Hand([],0)
PLAYER_HANDS = [Hand([],0)]
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
FONT = "Arial"
FONT_SIZE = 24
CARD_SIZE = 200

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
    return DECK
    
# Burn a card, show burn
def burn_card():
    print("[DBG] FUNC ENTRY: burn_card")
    burned_card = DECK.pop_card().get_card_symbol()
    print('\nburn card:', burned_card)
    return burned_card

def show_cards_hidden_dealer():
    print("[DBG] FUNC ENTRY: show_cards_hidden_dealer")
    # show some cards
    print("\n\n\n\n\n\n\n\n\n\n\nDEALER\n", DEALER_HAND.cards[0].get_card_symbol(), CARD_SYMBOLS[0])
    print(DEALER_HAND.count - DEALER_HAND.cards[1].value)

    player_hands_output = ""
    for hand in PLAYER_HANDS:
        print("\nPLAYER\n", hand)
        player_hands_output = player_hands_output + (str)(hand)

    GUI_text_dealer.config(text=DEALER_HAND.cards[0].get_card_symbol() + CARD_SYMBOLS[0], font=(FONT, CARD_SIZE))
    GUI_text_player.config(text=player_hands_output, font=(FONT, CARD_SIZE))

def show_cards_flipped_dealer():
    # show all cards
    print("\n\n\n\n\n\n\n\n\n\n\nDEALER\n", DEALER_HAND)
    for hand in PLAYER_HANDS:
        print("\nPLAYER\n", hand)

def draw():
    print("[DBG] FUNC ENTRY: draw")
    # Player, dealer, player, dealer, yes it matters
    PLAYER_HANDS[0].add_card(DECK.pop_card())
    DEALER_HAND.add_card(DECK.pop_card())
    PLAYER_HANDS[0].add_card(DECK.pop_card())
    DEALER_HAND.add_card(DECK.pop_card())

    show_cards_hidden_dealer()

    # Does dealer have BlackJack?
    if DEALER_HAND.count == 21:
        if PLAYER_HANDS[0].count != 21:
            print("\nDealer has BlackJack!")
        else:
            print("push.... BlackJack = BlackJack")
        show_cards_flipped_dealer()
        cleanup_table()
        draw()
    # Does the player have BlackJack?
    elif PLAYER_HANDS[0].count == 21: 
        print("\nplayer has BlackJack!")
        show_cards_flipped_dealer()

def surrender(hand):
    print("\nplayer surrendered hand")
    hand.clear_hand()
    hand.stand = True

def stand(hand):
    print("\nplayer stands")
    hand.stand = True

def hit(hand):
    print("\n\n\n\n\n\n\n\n\n\nplayer hits")
    hand.add_card(DECK.pop_card())
    if hand.count > 21:
        show_cards_flipped_dealer()
        print("\n\nplayer bust!")
        hand.stand = True
        time.sleep(2)
    else:
        show_cards_hidden_dealer()

def double(hand):
    print("\n\n\n\n\n\n\n\n\n\nplayer doubles")
    hand.add_card(DECK.pop_card())
    show_cards_hidden_dealer()
    hand.stand = True

def split(hand):
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

def player_loop(player_choice):
    print("[DBG] FUNC ENTRY: player_loop")
    # Player has some options
    for hand in PLAYER_HANDS:
        while not hand.stand:
            show_cards_hidden_dealer()
            print("\n0: surrender\n1: stand\n2: hit\n3: double")
            # if matching card value pair, split is available. note you can only split IFF 2 cards in a hand
            if len(hand.cards) == 2:
                if PLAYER_HANDS[0].cards[0].value == PLAYER_HANDS[0].cards[1].value:
                    print("4: split")
                    GUI_button_split.config(state=ACTIVE)
            
            if player_choice == 0:
                surrender(hand)
            elif player_choice == 1:
                stand(hand)
            elif player_choice == 2:
                hit(hand)
            elif player_choice == 3:
                double(hand)
            elif player_choice == 4:
                split(hand)

def dealer_loop():
    print("[DBG] FUNC ENTRY: dealer_loop")
    global PLAYER_WINS, DEALER_WINS, TOTAL_HANDS
    show_cards_flipped_dealer()
    time.sleep(1)

    if len(PLAYER_HANDS) == 1 and (PLAYER_HANDS[0].count == 0 or PLAYER_HANDS[0].count > 21):
        show_cards_flipped_dealer()
        DEALER_WINS += 1
        print("dealer win")
        TOTAL_HANDS += 1
    else:
        while DEALER_HAND.count < 17:
            DEALER_HAND.add_card(DECK.pop_card())
            show_cards_flipped_dealer()
            time.sleep(1)

        if DEALER_HAND.count > 21:
            print("dealer bust")
            PLAYER_WINS += 1
            TOTAL_HANDS += 1
        else:
            for hand in PLAYER_HANDS:
                if DEALER_HAND.count == hand.count:
                    print("push")
                    print("{} = {}".format(DEALER_HAND.count, hand.count))
                else:
                    if DEALER_HAND.count > hand.count or hand.count > 21:
                        DEALER_WINS += 1
                        print("dealer win")
                    else:
                        print("player win")
                        PLAYER_WINS += 1
                    print("{} > {}".format(DEALER_HAND.count, hand.count))
            TOTAL_HANDS += 1
    time.sleep(1)

#DECK = create_shuffle_deck(NUMBER_OF_DECKS)
#burn_card()
#
#while (len(DECK.cards) > CUT_CARD_COUNT):
#    cleanup_table()
#    draw()
#    player_loop()
#    dealer_loop()
#
#print ("\ngame over! stats:\nplayer wins:{}\ndealer wins:{}\nwin:{:.2%}".format(PLAYER_WINS, DEALER_WINS, PLAYER_WINS / TOTAL_HANDS))

##### Game Window
GUI_game_window = tkinter.Tk()
GUI_game_window.title("blackjack")
GUI_game_window.geometry('{}x{}'.format(WINDOW_WIDTH, WINDOW_HEIGHT))

##### Menu
GUI_game_menu = tkinter.Menu(GUI_game_window)
GUI_game_menu_file_exit = tkinter.Menu(GUI_game_menu, tearoff=0)
def menu_eventhandler_exit():
    exit()
GUI_game_menu_file_exit.add_command(label="exit", command=menu_eventhandler_exit)
GUI_game_menu.add_cascade(label='file', menu=GUI_game_menu_file_exit)
GUI_game_window.config(menu=GUI_game_menu)

##### Top Text
GUI_text_blackjack = tkinter.Label(GUI_game_window, text="blackjack", font=(FONT, FONT_SIZE))
GUI_text_blackjack.grid(column=0, row=0)
#GUI_text_blackjack.pack(fill='both', expand=True)

GUI_text_deck_count = tkinter.Label(GUI_game_window, text="# decks", font=(FONT, FONT_SIZE))
GUI_text_deck_count.grid(column=0, row=1)
#GUI_text_deck_count.pack(fill='both', expand=True)

##### Entry Text
GUI_entry_num_decks = tkinter.Entry(GUI_game_window, font=(FONT, FONT_SIZE))
#GUI_entry_num_decks.pack(fill='both', expand=True)
GUI_entry_num_decks.grid(column=1, row=1)

##### Dealer Text
GUI_text_dealer = tkinter.Label(GUI_game_window, text="", font=(FONT, FONT_SIZE))
GUI_text_dealer.grid(column=0, row=4)
#GUI_text_blackjack.pack(fill='both', expand=True)

##### Player Text
GUI_text_player = tkinter.Label(GUI_game_window, text="", font=(FONT, FONT_SIZE))
GUI_text_player.grid(column=0, row=5)
#GUI_text_blackjack.pack(fill='both', expand=True)


##### Buttons
def button_eventhandler_start():
    try:
        NUMBER_OF_DECKS = (int)(GUI_entry_num_decks.get())
    except:
        NUMBER_OF_DECKS = 6
    DECK = create_shuffle_deck(NUMBER_OF_DECKS)
    GUI_entry_num_decks.destroy()
    GUI_text_blackjack.config(text = "burned card:")
    GUI_text_dealer.config(text="dealer cards", font=(FONT, FONT_SIZE))
    GUI_text_player.config(text="player cards", font=(FONT, FONT_SIZE))
    GUI_text_deck_count.config(text = burn_card(), font=(FONT, CARD_SIZE))
    GUI_button_start.destroy()
    GUI_button_draw.config(state=ACTIVE)

def button_eventhandler_draw():
    GUI_text_blackjack.config(text = "")
    GUI_text_deck_count.config(text = "")
    GUI_text_dealer.grid(column=0, row=0)
    GUI_text_player.grid(column=0, row=1)
    GUI_button_draw.destroy()
    draw()
    GUI_button_surrender.config(state=ACTIVE)
    GUI_button_stand.config(state=ACTIVE)
    GUI_button_hit.config(state=ACTIVE)
    GUI_button_double.config(state=ACTIVE)

def button_eventhandler_surrender():
    player_loop(0)
    dealer_loop()

def button_eventhandler_stand():
    player_loop(1)

def button_eventhandler_hit():
    player_loop(2)

def button_eventhandler_double():
    player_loop(3)

def button_eventhandler_split():
    player_loop(4)


GUI_button_start = tkinter.Button(GUI_game_window, text="start!", font=(FONT, FONT_SIZE), command=button_eventhandler_start)
GUI_button_start.grid(column=0, row=3)
#GUI_button_start.pack(fill='both', expand=True)

GUI_button_draw = tkinter.Button(GUI_game_window, text="draw", font=(FONT, FONT_SIZE), state=DISABLED, command=button_eventhandler_draw)
GUI_button_draw.grid(column=0, row=6)

GUI_button_surrender = tkinter.Button(GUI_game_window, text="surrender", font=(FONT, FONT_SIZE), state=DISABLED, command=button_eventhandler_surrender)
GUI_button_surrender.grid(column=1, row=6)

GUI_button_stand = tkinter.Button(GUI_game_window, text="stand", font=(FONT, FONT_SIZE), state=DISABLED, command=button_eventhandler_stand)
GUI_button_stand.grid(column=2, row=6)

GUI_button_hit = tkinter.Button(GUI_game_window, text="hit", font=(FONT, FONT_SIZE), state=DISABLED, command=button_eventhandler_hit)
GUI_button_hit.grid(column=3, row=6)

GUI_button_double = tkinter.Button(GUI_game_window, text="double", font=(FONT, FONT_SIZE), state=DISABLED, command=button_eventhandler_double)
GUI_button_double.grid(column=4, row=6)

GUI_button_split = tkinter.Button(GUI_game_window, text="split", font=(FONT, FONT_SIZE), state=DISABLED, command=button_eventhandler_split)
GUI_button_split.grid(column=5, row=6)

GUI_game_window.mainloop()