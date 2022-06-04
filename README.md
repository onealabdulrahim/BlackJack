# BlackJack
Python GUI-based lightweight Blackjack app. Features real-time card tracking within user-adjustable deck count. Psuedorandom shuffling.

![screenshot](https://github.com/onealabdulrahim/BlackJack/blob/master/screens/Animation.gif)

## Key Features

* GUI-based: simple buttons for advancing gameplay
* Lightweight: ascii symbols for cards, on-the-fly card counts
* Psuedorandom: as fair as it can get (although, it seems the dealer wins a lot, so I need to work on my basic strategy)

## Implementation Features

* Object oriented: Suit > Card > Hand > Deck
* Blocking algorithm: card dealing is in order, w.r.t. real-life BlackJack conventions
* Custom queue implementation for deck

## How To Use

* Requires python and package dependencies: tkinter
* Extract .py files to the same directory
* Execute the GUI with python
```
> python Blackjack_GUI.py
```

## Screenshots
![screenshot](https://github.com/onealabdulrahim/BlackJack/blob/master/screens/shuffled.png)
![screenshot](https://github.com/onealabdulrahim/BlackJack/blob/master/screens/hitting.png)
