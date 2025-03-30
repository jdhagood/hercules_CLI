from commands.command import Command
import curses


cerberus_ascii_art ="""
                            /\_/\____,
                  ,___/\_/\ \  ~     /
                  \     ~  \ )   XXX
                    XXX     /    /\_/\___,
                       \o-o/-o-o/   ~    /
                        ) /     \    XXX
                       _|    / \ \_/
                    ,-/   _  \_/   \\
                   / (   /____,__|  )
                  (  |_ (    )  \) _|
                 _/ _)   \   \__/   (_
                (,-(,(,(,/      \,),),)\n
"""
class Underworld(Command):
    def execute(self, terminal, args):
        if not args:
            self.error(terminal)
            return
        
        if args[0] in ("-h", "--h"):
            self.help(terminal)
            return
        
        if len(args) >= 2 and args[0] in ("-add", "--add") and args[1] == "kerberos":
            self.add_kerbs(terminal)
            return

        self.error(terminal)

    def add_kerbs(self, terminal):
        display_text = terminal.get_history()[::]
        
        display_text.append((cerberus_ascii_art, "red"))
        display_text.append(("", "White"))

        kerbs = []
        input_str = ""
        while True:
            kerb_str_list = ""
            for kerb in kerbs:
                kerb_str_list += f"Enter Hades: {kerb}\n"
            kerb_str_list += f"Enter Hades: {input_str}"
            display_text[-1] = (kerb_str_list, "white")
            terminal.print_colored_text(display_text)
            key = terminal.stdscr.getch()
            if key == 10:  # Enter key
                if not input_str:
                    break

                kerbs.append(input_str)
                input_str = ""
            elif key in (curses.KEY_BACKSPACE, 8):
                input_str = input_str[:-1]
            elif 32 <= key <= 126:
                input_str += chr(key)
        
        display_text.append(("\n\n", "white"))
        terminal.set_history(display_text)


    def help(self, terminal):
        terminal.append_history(("Good luck\n\n", "white"))

    def error(self, terminal):
        terminal.append_history(("The syntax of the command is incorrect\n\n", "red"))