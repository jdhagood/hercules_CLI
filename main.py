# main.py
import curses
from cli_objects.directory import Directory
from cli_objects.file import File
from cli_objects.user import User
from display import init_terminal, display_terminal

from command_manager import CommandManager

from terminal import Terminal

terminal = Terminal()

def main(stdscr):
    # USER SETUP
    root = Directory("root")
    root.add_content(File("hercules", "txt", "Hello World"))
    root.add_content(File("ballz", "txt", "Goodbye World"))
    A = Directory("A")
    A.add_content(Directory("B"))
    root.add_content(A)
    root.add_content(Directory("C"))
    user = User("Hercules", root)

    init_terminal(stdscr)
    command_manager = CommandManager()
    
    command = ""

    while True:
        display_terminal(user, command, stdscr)

        key = stdscr.getch()
        if key == 10:  # Enter key
            if command.strip():
                command_manager.execute(command, user)
            command = ""
        elif key == 27:  # Escape key to exit
            break
        elif key in (curses.KEY_BACKSPACE, 8):
            command = command[:-1]
        elif key == curses.KEY_UP:
            pass  # implement up and down scrolling
        elif key == curses.KEY_DOWN:
            pass
        elif 32 <= key <= 126:
            command += chr(key)

if __name__ == "__main__":
    curses.wrapper(terminal.run)