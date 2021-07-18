"""
BlackJack_GUI.py

GUI implementation

As part of the Blackjack suite
@author Oneal Abdulrahim
"""

import tkinter as tk
from tkinter.constants import ACTIVE, DISABLED
import BlackJack
import time

global DECK
CUT_CARD_COUNT = 10
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 800
FONT = "Consolas"
FONT_SIZE = 24
CARD_SIZE = 150


class BlackJack_Navbar(tk.Menu):
    def __init__(self, gui, *args, **kwargs):
        tk.Menu.__init__(self, *args, **kwargs)
        self.gui = gui

        self.menu = tk.Menu(self.gui)
        self.make_game_menu()
        self.gui.config(menu=self.menu)
        
    def make_game_menu(self):
        file = tk.Menu(self.menu, tearoff=0)
        file.add_command(label="restart", command=self.gui.restart_window)
        file.add_command(label="exit", command=self.gui.close_window)
        self.menu.add_cascade(label="game", menu=file)

class BlackJack_Window(tk.Frame):
    def __init__(self, gui, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.gui = gui

        self.screen_start_game()
        self.pack(side="top", expand=True, fill="both")

    def clear_window(self):
        self.pack_forget()
        for item in self.winfo_children():
            item.destroy()

    def screen_start_game(self):
        main_menu_text = tk.Label(self, text="blackjack", font=(FONT, FONT_SIZE))
        start_button = tk.Button(self, text="start!",  font=(FONT, FONT_SIZE), command=self.screen_shuffle_decks)

        main_menu_text.pack(fill="both", expand=True)
        start_button.pack(fill="both", expand=True)

    def screen_shuffle_decks(self):
        self.clear_window()
        
        DECK_COUNTS = [1, 2, 3, 4, 5, 6, 7, 8]
        deck_count_list = tk.StringVar(self)
        deck_count_list.set(DECK_COUNTS[5]) # default is index 5, for 6 decks
        deck_count_dropdown = tk.OptionMenu(self, deck_count_list, *DECK_COUNTS)
        deck_count_dropdown.config(font=(FONT, FONT_SIZE))
        sub_menu = self.nametowidget(deck_count_dropdown.menuname)
        sub_menu.config(font=(FONT, FONT_SIZE))

        num_deck_text = tk.Label(self, text="# of decks", font=(FONT, FONT_SIZE))
        shuffle_button = tk.Button(self, text="shuffle!",  font=(FONT, FONT_SIZE), command=lambda: self.screen_burn_card((int)(deck_count_list.get())))

        num_deck_text.pack(fill="both", expand=True)
        deck_count_dropdown.pack(fill="both", expand=True)
        shuffle_button.pack(fill="both", expand=True)
        self.pack(side="top", expand=True, fill="both")
    
    def screen_burn_card(self, num_decks):
        self.clear_window()
        
        global DECK
        DECK = BlackJack.create_shuffle_deck(num_decks)

        burn_card_text = tk.Label(self, text="shuffling! total decks: {NUMBER_OF_DECKS}\nburned a card...".format(NUMBER_OF_DECKS = num_decks), font=(FONT, FONT_SIZE))
        burn_card_disp = tk.Label(self, text=BlackJack.burn_card(DECK), font=(FONT, CARD_SIZE))
        draw_button = tk.Button(self, text="draw",  font=(FONT, FONT_SIZE), command=self.screen_initial_draw)

        burn_card_text.pack(fill="both", expand=True)
        burn_card_disp.pack(fill="both", expand=True)
        draw_button.pack(fill="both", expand=True)
        self.pack(side="top", expand=True, fill="both")

    def screen_initial_draw(self):
        
        self.clear_window()
        BlackJack.initial_draw(DECK)
        print("num cards left in the deck: {}".format(len(DECK.cards)))
        self.update_cards()

        check_blackjack = BlackJack.check_blackjack()

        if check_blackjack == -1:
            self.screen_final("dealer blackjack")
        elif check_blackjack == 0:
            self.screen_final("push")
        elif check_blackjack == 1:
            self.screen_final("player blackjack")

        for hand in BlackJack.PLAYER_HANDS:
            if not hand.stand:
                if len(hand.cards) == 2:
                    if BlackJack.PLAYER_HANDS[0].cards[0].value == BlackJack.PLAYER_HANDS[0].cards[1].value:
                        self.split_button.config(state=ACTIVE)
        self.pack(side="top", expand=True, fill="both")


    def button_eventhandler_surrender(self, hand):
        BlackJack.surrender(hand)
        self.screen_final("player surrenders")

    def button_eventhandler_stand(self, hand):
        BlackJack.stand(hand)
        self.dealer_draw()

    def button_eventhandler_hit(self, hand):
        BlackJack.hit(hand, DECK)
        if hand.count > 21:
            hand.stand = True
            self.screen_final("player bust")
        else:
            self.update_cards()

    def button_eventhandler_double(self, hand):
        BlackJack.double(hand, DECK)
        self.dealer_draw()

    def button_eventhandler_split(self, hand):
        BlackJack.split(hand, DECK)
        self.update_cards()

    def dealer_draw(self):
        self.update_dealer_cards()
        if len(BlackJack.PLAYER_HANDS) == 1 and (BlackJack.PLAYER_HANDS[0].count == 0 or BlackJack.PLAYER_HANDS[0].count > 21):
            self.screen_final("dealer win")
        else:
            while BlackJack.DEALER_HAND.count < 17:
                self.update_dealer_cards()
                self.gui.update()
                self.after(1000, BlackJack.dealer_draw(DECK))
            if BlackJack.DEALER_HAND.count > 21:
                self.screen_final("dealer bust")
            else:
                for hand in BlackJack.PLAYER_HANDS:
                    if BlackJack.DEALER_HAND.count == hand.count:
                        print("push")
                        print("{} = {}".format(BlackJack.DEALER_HAND.count, hand.count))
                        self.screen_final("push")
                    else:
                        if BlackJack.DEALER_HAND.count > hand.count or hand.count > 21:
                            print("dealer win")
                            self.screen_final("dealer win")
                        else:
                            print("player win")
                            self.screen_final("player win")     

    def update_dealer_cards(self):
        self.clear_window()
        self.dealer_hand = tk.Label(self, text=BlackJack.DEALER_HAND.__str__(), font=(FONT, CARD_SIZE))

        all_player_hands_output = ""
        for hand in BlackJack.PLAYER_HANDS:
            all_player_hands_output += hand.__str__() + ""

        self.player_hand = tk.Label(self, text=all_player_hands_output, font=(FONT, CARD_SIZE))
        self.dealer_hand.pack(fill="both", expand=True)
        self.player_hand.pack(fill="both", expand=True)
        self.pack(side="top", expand=True, fill="both")

    def update_cards(self):
        self.clear_window()
        self.dealer_hand = tk.Label(self, text=(str)(BlackJack.DEALER_HAND.cards[0].get_card_symbol() + BlackJack.CARD_SYMBOLS[0]), font=(FONT, CARD_SIZE))

        all_player_hands_output = ""
        for hand in BlackJack.PLAYER_HANDS:
            all_player_hands_output += hand.__str__() + ""

        self.player_hand = tk.Label(self, text=all_player_hands_output, font=(FONT, CARD_SIZE))

        self.dealer_hand.pack(fill="both", expand=True)
        self.player_hand.pack(fill="both", expand=True)

        self.surrender_button = tk.Button(self, text="surrender",  font=(FONT, FONT_SIZE), command=lambda: self.button_eventhandler_surrender(hand))
        self.stand_button = tk.Button(self, text="stand    ",  font=(FONT, FONT_SIZE), command=lambda: self.button_eventhandler_stand(hand))
        self.hit_button = tk.Button(self, text="hit      ",  font=(FONT, FONT_SIZE), command=lambda: self.button_eventhandler_hit(hand))
        self.double_button = tk.Button(self, text="double   ",  font=(FONT, FONT_SIZE), command=lambda: self.button_eventhandler_double(hand))
        self.split_button = tk.Button(self, text="split    ",  font=(FONT, FONT_SIZE), state=DISABLED, command=lambda: self.button_eventhandler_split(hand))

        self.surrender_button.pack(fill="both", expand=False)
        self.stand_button.pack(fill="both", expand=False)
        self.hit_button.pack(fill="both", expand=False)
        self.double_button.pack(fill="both", expand=False)
        self.split_button.pack(fill="both", expand=False)
        self.pack(side="top", expand=True, fill="both")

    def screen_final(self, text):
        self.clear_window()
        self.dealer_hand = tk.Label(self, text=BlackJack.DEALER_HAND.__str__(), font=(FONT, CARD_SIZE))

        all_player_hands_output = ""
        for hand in BlackJack.PLAYER_HANDS:
            all_player_hands_output += hand.__str__() + ""

        self.player_hand = tk.Label(self, text=all_player_hands_output, font=(FONT, CARD_SIZE))
        self.player_text = tk.Label(self, text=text, font=(FONT, FONT_SIZE))
        new_game_button = tk.Button(self, text="new hand",  font=(FONT, FONT_SIZE), command=self.screen_initial_draw)
        end_game_button = tk.Button(self, text="game over!",  font=(FONT, FONT_SIZE), command=self.gui.close_window)
        self.dealer_hand.pack(fill="both", expand=True)
        self.player_hand.pack(fill="both", expand=True)
        self.player_text.pack(fill="both", expand=True)
        if len(DECK.cards) > CUT_CARD_COUNT:
            new_game_button.pack(fill="both", expand=True)
        else:
            end_game_button.pack(fill="both", expand=True)
        self.pack(side="top", expand=True, fill="both")

class BlackJack_GUI(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("blackjack")
        self.geometry("{}x{}".format(WINDOW_WIDTH, WINDOW_HEIGHT))
    
    def restart_window(self):
        self.close_window()
        main()

    def close_window(self):
        self.destroy()

def main():
    gui = BlackJack_GUI()
    window = BlackJack_Window(gui)
    menu = BlackJack_Navbar(gui)
    gui.mainloop()

if __name__ == "__main__":
    main()