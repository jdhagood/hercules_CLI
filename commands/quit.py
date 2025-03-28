from commands.command import Command

class Quit(Command):
    def execute(self, terminal, args):
        quit()