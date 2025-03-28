import curses
from terminal import Terminal
from cli_objects.user import User
from cli_objects.directory import Directory
from cli_objects.file import File
from command_manager import CommandManager

# Example setup
root = Directory("root")
root.add_content(File("hercules", "txt", "Hello World"))
root.add_content(File("test", "txt", "Goodbye World", password = "123", lockout_time=30))
A = Directory("A")
A.add_content(Directory("B", password="abc"))
root.add_content(A)
root.add_content(Directory("C"))
user = User("Hercules", root) # name and starting working dir
user = User("Hercules", root)


command_manager = CommandManager()
terminal = Terminal(user, root, command_manager)

if __name__ == "__main__":
    curses.wrapper(terminal.curses_entry)