import curses

def print_colored_text(stdscr, text_tuples):
    # Initialize color pairs
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK)

    stdscr.clear()
    
    y, x = 0, 0  # Start position

    for text, color in text_tuples:
        for char in text:
            if char == '\n':
                y += 1  # Move to the next line
                x = 0   # Reset column position
            else:
                stdscr.addstr(y, x, char, curses.color_pair(color))
                x += 1  # Move to the next column

    stdscr.refresh()
    stdscr.getch()  # Wait for a key press before exiting

def main():
    text_tuples = [
        ("Hello, ", 1),
        ("Red!", 1),
        (" This ", 2),
        ("is green.\n", 2),
        ("New line in ", 3),
        ("blue.", 3)
    ]
    curses.wrapper(print_colored_text, text_tuples)

if __name__ == "__main__":
    main()
