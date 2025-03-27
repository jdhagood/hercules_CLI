from commands.command import Command

class Quit(Command):
    def execute(self, user, args):
        quit()