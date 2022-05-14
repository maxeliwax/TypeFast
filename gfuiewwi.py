def wpm_test(stdscr):
    target_sentense = "jag heter Max jag har bor i STORMAKTEN SVERIGE" #en test text 
    current_text = []
    stdscr.clear()
    stdscr.addstr(target_sentense)
    stdscr.refresh()
    

    while True:#skapar en loop som ska loopa GETKEY detta registerar dina knabbtryck 
        key = stdscr.getkey()
        current_text.append(key)
        for char in current_text:
            stdscr.addstr(char,curses.color_pair(1))

        stdscr.refresh()

   



    
    



wrapper(main)









while True:#skapar en loop som ska loopa GETKEY detta registerar dina knabbtryck 
        key = stdscr.getkey()
        current_text.append(key)
        for char in current_text:
            stdscr.addstr(char,curses.color_pair(1))
            stdscr.refresh()