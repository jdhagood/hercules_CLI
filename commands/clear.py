from commands.command import Command

class Clear(Command):
    def execute(self, terminal, args):
        terminal.set_history([])