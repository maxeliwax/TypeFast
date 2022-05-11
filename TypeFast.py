#Maximilian Walldov 
#TypeFast 
#teinf-20
#2022 VT

import curses
from curses import wrapper


def main(stdscr):
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_YELLOW) #detta skapar en bakrunds färg så det är  vit text och gul bakrund 

    stdscr.clear()
    stdscr.addstr(3, 45, "wellcome to FastType", curses.color_pair(1))
    stdscr.addstr(5, 49,"\npress any key to begin ", curses.COLOR_RED)
    stdscr.refresh()
    stdscr.getkey() #registerar vad du trycker på
    
    



wrapper(main)
