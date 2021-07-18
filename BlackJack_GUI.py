'''
BlackJack_GUI.py

GUI implementation

As part of the Blackjack suite
@author Oneal Abdulrahim
'''
import tkinter
from BlackJack import *

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

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
GUI_text_blackjack = tkinter.Label(GUI_game_window, text="blackjack", font=("Arial", 36))
GUI_text_blackjack.grid(column=0, row=0, sticky=tkinter.N)
#GUI_text_blackjack.pack(fill='both', expand=True)
GUI_text_deck_count = tkinter.Label(GUI_game_window, text="number of decks", font=("Arial", 24))
GUI_text_deck_count.grid(column=0, row=1, sticky=tkinter.N)
#GUI_text_deck_count.pack(fill='both', expand=True)
GUI_text_deck_count = tkinter.Label(GUI_game_window, text="# decks", font=("Arial", 24))


##### Entry Text
GUI_entry_num_decks = tkinter.Entry(GUI_game_window, font=("Arial", 24))
#GUI_entry_num_decks.pack(fill='both', expand=True)
GUI_entry_num_decks.grid(column=1, row=1, sticky=tkinter.N)

##### Dealer Text

##### Player Text



##### Buttons
def button_eventhandler_start():
    pass

GUI_button_start = tkinter.Button(GUI_game_window, text="start!", font=("Arial", 24), command=button_eventhandler_start)
GUI_button_start.grid(column=0, row=3)
#GUI_button_start.pack(fill='both', expand=True)


GUI_game_window.mainloop()