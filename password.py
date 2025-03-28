import curses
import time

class Password:
    def __init__(self, password, lockout_time = 0):
        self.password = password
        if lockout_time:
            self.lockout_time = lockout_time
            self.has_lockout = True
            self.last_incorrect_guess_time = -float("inf")
        else:
            self.has_lockout = False
    
    def get_password(self):
        return self.password
    
    def set_password(self, password):
        self.password = password

    def is_lockedout(self):
        return time.time() < self.last_incorrect_guess_time + self.lockout_time
    
    def lockout_time_remaining(self):
        return int(max(0, self.last_incorrect_guess_time + self.lockout_time  - time.time()))

    def enter_password(self, terminal):
        display_text = terminal.get_history()[::]
        display_text.append(("This File or Directory is password protected\n\n", "red"))

        display_text.append(("Enter Password: ", "white"))
        
        entered_password = ""
        while True:
            display_text[-1] = ("Enter Password: " + entered_password, "white")
            terminal.print_colored_text(display_text)
            key = terminal.stdscr.getch()
            if key == 10:  # Enter key
                break
            elif key in (curses.KEY_BACKSPACE, 8):
                entered_password = entered_password[:-1]
            elif 32 <= key <= 126:
                entered_password += chr(key)
        
        display_text[-1] = ("Enter Password: " + entered_password + "\n\n", "white")
        terminal.set_history(display_text)
        if entered_password == self.password:
            return True
        else:
            self.last_incorrect_guess_time = time.time()
            return False
