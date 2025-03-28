import curses
from cli_objects.directory import Directory
from cli_objects.file import File
from cli_objects.user import User

class Terminal:
    def __init__(self, user, root, command_manager):
        self.user = user
        self.root = root
        self.command_manager = command_manager
        self.text_input = ""

        self.display_history = []
        self.command_history = []

    def get_history(self):
        return self.display_history

    def append_history(self, new_history):
        self.display_history.append(new_history)

    def extend_history(self, new_history):
        self.display_history.extend(new_history)
    
    def set_history(self, new_history):
        self.display_history = new_history

    def curses_entry(self, stdscr):
        self.stdscr = stdscr
        self.run()

    def run(self):
        self.init_terminal()

        command_pointer = -1
        while True:
            self.display()
            key = self.stdscr.getch()
            if key == 10:  # Enter key
                if self.text_input.strip():
                    command_pointer = -1
                    self.command_history.insert(0, self.text_input)
                    self.command_manager.execute(self.text_input, self)
                self.text_input = ""
            elif key == 27:  # Escape key to exit
                break
            elif key in (curses.KEY_BACKSPACE, 8):
                command_pointer = -1
                self.text_input = self.text_input[:-1]
            elif key == curses.KEY_UP:
                if command_pointer < len(self.command_history)-1:
                    command_pointer += 1
                    self.text_input = self.command_history[command_pointer]
            elif key == curses.KEY_DOWN:
                if command_pointer > 0:
                    command_pointer -= 1
                    self.text_input = self.command_history[command_pointer]
            elif 32 <= key <= 126:
                command_pointer = -1
                self.text_input += chr(key)
    
    def init_terminal(self):
        # COLOR SETUP
        curses.start_color()
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)
        curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK)
        curses.init_pair(5, curses.COLOR_WHITE, curses.COLOR_BLACK)

        global color_dict
        color_dict = {
            "red": 1,
            "green": 2,
            "blue": 3,
            "yellow": 4,
            "white": 5
        }

        curses.curs_set(1)
        self.stdscr.clear()

    def display(self):
        text_tuples = self.display_history[::]
        text_tuples.extend(self.user.get_terminal_string(self.text_input))
        self.print_colored_text(text_tuples)

    def print_colored_text(self, text_tuples):
        def wrap_tuples(text_tuples, max_width, max_height):
            text_rows = []
            current_row = []
            current_line = ""
            line_width = 0

            for text, color in text_tuples:
                for char in text:
                    if char == '\n': 
                        current_row.append((current_line + '\n', color))  # Add completed line
                        text_rows.append(current_row.copy())  # Store the row
                        current_row = []  # Reset for the next line
                        current_line = ""
                        line_width = 0
                    elif line_width >= max_width - 1:  # Wrap text
                        current_row.append((current_line, color))
                        text_rows.append(current_row.copy())
                        current_row = []
                        current_line = char  # Start new line with the current character
                        line_width = 1
                    else:
                        current_line += char
                        line_width += 1
                
                if current_line:
                    current_row.append((current_line, color))
                    current_line = ""

            # Add the last unfinished line, if any
            if current_row or current_line:
                current_row.append((current_line, color))
                text_rows.append(current_row.copy())

            # **Keep only the last `max_height` lines**
            wrapped_tuples = []
            for line in text_rows[-max_height:]:
                wrapped_tuples.extend(line)

            return wrapped_tuples

        max_height, max_width = self.stdscr.getmaxyx()
        self.stdscr.clear()
        
        y, x = 0, 0  # Start position

        trimmed_tuples = wrap_tuples(text_tuples, max_width, max_height)

        for text, color in trimmed_tuples:
            for char in text:
                if char == '\n':  
                    y += 1
                    x = 0
                else:
                    if x >= max_width - 1:  # Wrap if we reach the end of the line
                        y += 1
                        x = 0
                    
                    if y >= max_height - 1:  # Stop printing if we reach the bottom
                        return  # Stop processing if we run out of space
                    
                    self.stdscr.addstr(y, x, char, curses.color_pair(color_dict.get(color, 0)))
                    x += 1  

        self.stdscr.refresh()
