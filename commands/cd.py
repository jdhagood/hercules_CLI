from commands.command import Command
from cli_objects.directory import Directory

class Cd(Command):
    def execute(self, terminal, args):
        if not args:
            return
        
        new_dir = args[0]

        if new_dir == '..':
            if terminal.user.get_working_dir().get_name() != "root":
                terminal.user.pop_path()
                terminal.append_history(("\n", "white"))
            return

        for content in terminal.user.get_working_dir().get_contents():
            if isinstance(content, Directory) and content.get_name() == new_dir:
                if content.has_password:
                    if content.password.has_lockout == True:
                        if content.password.is_lockedout():
                            terminal.append_history((f"This directory is locked for {content.password.lockout_time_remaining()} more seconds\n\n", "red"))
                            return
                    if content.ask_password(terminal) == False:
                        if content.password.has_lockout:
                            terminal.append_history((f"Incorrect Password! Locked for {content.password.lockout_time} seconds!\n\n", "red"))
                            return
                        terminal.append_history(("Incorrect Password!\n\n", "red"))
                        return
                    terminal.append_history(("Corret Password\n\n", "green"))
                

                terminal.user.append_path(content)
                terminal.append_history(("\n", "white"))
                return
        
        terminal.append_history(("The system cannot find the path specified.\n\n", "red"))