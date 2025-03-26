import curses

def login_screen(stdscr):
    password = "hercules"
    user_guess = "bro"

    header = """\                                            
    ██╗      ██████╗  ██████╗ ██╗███╗   ██╗
    ██║     ██╔═══██╗██╔════╝ ██║████╗  ██║
    ██║     ██║   ██║██║  ███╗██║██╔██╗ ██║
    ██║     ██║   ██║██║   ██║██║██║╚██╗██║
    ███████╗╚██████╔╝╚██████╔╝██║██║ ╚████║
    ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝╚═╝  ╚═══╝                                                 
    """ # ANSI Shadow

    # Initialize colors
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_WHITE)
    curses.init_pair(4, curses.COLOR_RED, curses.COLOR_WHITE)
    curses.init_pair(5, curses.COLOR_BLACK, curses.COLOR_GREEN)
    curses.init_pair(6, curses.COLOR_BLACK, curses.COLOR_MAGENTA)

    RED_AND_BLACK = curses.color_pair(1)
    GREEN_AND_BLACK = curses.color_pair(2)
    GREEN_AND_WHITE = curses.color_pair(3)
    RED_AND_WHITE = curses.color_pair(4)
    BLACK_AND_GREEN = curses.color_pair(5)
    BLACK_AND_MAGENTA = curses.color_pair(6)

    def show_screen():
        stdscr.clear()
        stdscr.addstr(header + '\n', GREEN_AND_BLACK)

        stdscr.addstr("EMPLOYEE ID: " + user_guess, RED_AND_BLACK)

        stdscr.refresh()

    while True:
        show_screen()
        key = stdscr.getch()

        if key == ord('\n'):
            if user_guess == password:
                return
            else:
                user_guess = ""
        elif key in (127, curses.KEY_BACKSPACE, 8):  # Handle backspace
            user_guess = user_guess[:-1]
        elif key >= 32 and key <= 126:  # Printable ASCII
            user_guess += chr(key)
        




