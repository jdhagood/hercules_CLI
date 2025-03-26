import curses
from login import login_screen
from directory import Directory
from file import File
from user import User
from commands import execute_command
from display import display_terminal


def main(stdscr):
    """
    USER SETUP
    """
    root = Directory("root")
    root.add_content(File("hercules", "txt", "Hello World"))
    root.add_content(File("ballz", "txt", "Goodbye World"))
    A = Directory("A")
    A.add_content(Directory("B"))

    root.add_content(A)
    root.add_content(Directory("C"))
    user = User("Hercules", root)

    """
    COLOR SETUP
    """
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_WHITE, curses.COLOR_BLACK)


    color_dict = {
        "red": 1,
        "green": 2,
        "blue": 3,
        "yellow": 4,
        "white": 5
    }


    curses.curs_set(1)
    stdscr.clear()
    
    command = ""

    while True:
        display_terminal(user, command, color_dict, stdscr)

        key = stdscr.getch()
        
        if key == 10:  # Enter key
            if command.strip():
                execute_command(command, user)
            command = ""
        elif key == 27:  # Escape key to exit
            break
        elif key in (curses.KEY_BACKSPACE, 8):
            command = command[:-1]
        elif key == curses.KEY_UP:
            pass # implement up and down scrolling
        elif key == curses.KEY_DOWN:
            pass
        elif 32 <= key <= 126:
            command += chr(key)


if __name__ == "__main__":
    #curses.wrapper(login_screen)
    curses.wrapper(main)