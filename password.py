from display import print_colored_text
import curses

class Password:
    def __init__(self, password):
        self.password = password
    
    def get_password(self):
        return self.password
    
    def set_password(self, password):
        self.password = password
    
    def enter_password(self, user, stdscr):
        display_text = user.get_history()[::]
        display_text.append(("This File or Directory is password protected\n\n", "red"))
        display_text.append(("Enter Password: ", "white"))
        
        entered_password = ""
        while True:
            display_text[-1] = ("Enter Password: " + entered_password, "white")
            print_colored_text(stdscr, display_text)
            key = stdscr.getch()
            if key == 10:  # Enter key
                break
            elif key in (curses.KEY_BACKSPACE, 8):
                entered_password = entered_password[:-1]
            elif 32 <= key <= 126:
                entered_password += chr(key)
        
        display_text[-1] = ("Enter Password: " + entered_password + "\n\n", "white")
        user.set_History = display_text
        return entered_password == self.password

