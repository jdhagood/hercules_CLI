from commands.command import Command

class Help(Command):
    def execute(self, terminal, args):
        terminal.append_history(("lol, good luck XD\n\n", "white"))