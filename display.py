import curses

def print_colored_text(stdscr, text_tuples, color_dict):
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

    max_height, max_width = stdscr.getmaxyx()
    stdscr.clear()
    
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
                
                stdscr.addstr(y, x, char, curses.color_pair(color_dict.get(color, 0)))
                x += 1  

    stdscr.refresh()

def display_terminal(user, command, color_dict, stdscr):
    text_tuples = user.get_history()[::]
    text_tuples.extend(user.get_terminal_string(command))
    print_colored_text(stdscr, text_tuples, color_dict)
