#Maximilian Walldov 
#TypeFast 
#teinf-20
#2022 VT

import curses
from curses import color_pair, wrapper

  

def main_meny(stdscr):
    stdscr.clear()
    stdscr.addstr(3, 45, "wellcome to FastType", curses.color_pair(1))
    stdscr.addstr(5, 49,"\npress any key to begin", curses.color_pair(2))
    stdscr.refresh()
    key = stdscr.getkey()
    print(key) #registerar vad du trycker på

def wpm_test(stdscr):
    target_sentense ="jag heter max"#en test text 
    current_text = []

    stdscr.clear()
    stdscr.addstr(10,50,target_sentense, curses.color_pair(2)) #skriver ut target_sentense på plats 10 vertical 50 horisontellt 
    stdscr.refresh()
    stdscr.getkey()
    while True:
    
   

    if c == 'q':
        break

def main(stdscr):
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_YELLOW) #detta skapar en bakrunds färg så det är  vit text och gul bakrund 
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLUE)
    main_meny(stdscr)#kallar på funktion
    wpm_test(stdscr)#kallar på funktion 





   

wrapper(main)
