from commands.command import Command
from cli_objects.directory import Directory
from cli_objects.file import File

class Cat(Command):
    def execute(self, terminal, args):
        if not args:
            return
        

        file_name = args[0]

        for content in terminal.user.get_working_dir().get_contents():
            if isinstance(content, File) and f"{content.get_name()}.{content.get_extension()}" == file_name:
                if content.has_password:
                    if content.password.has_lockout == True:
                        if content.password.is_lockedout():
                            terminal.append_history((f"This file is locked for {content.password.lockout_time_remaining()} more seconds\n\n", "red"))
                            return
                    if content.ask_password(terminal) == False:
                        if content.password.has_lockout:
                            terminal.append_history((f"Incorrect Password! Locked for {content.password.lockout_time} seconds!\n\n", "red"))
                            return
                        terminal.append_history(("Incorrect Password!\n\n", "red"))
                        return
                    terminal.append_history(("Corret Password\n\n", "green"))
                terminal.append_history((content.get_content() + "\n\n", "white"))
                return
        
        terminal.append_history((f"{file_name} not found\n\n", "red"))