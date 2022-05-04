#Maximilian Walldov 
#TypeFast 
#teinf-20
#2022 VT

import time


def startmenu(strtmen):
    strtmen.clear()
    strtmen.addstr("Welcome to TypeFast :-)")
    strtmen.addstr("press N to start a race")

def display_text(strt, target, current, Wpm=0):
    strtmen.addstr(target)
    strtmen.addstr(1, 0 , f"Wpm): {Wpm}")

for i, char in enumerate(current):
    current_char 