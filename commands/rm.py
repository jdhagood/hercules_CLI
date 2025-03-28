from commands.command import Command

class Rm(Command):
    def execute(self, terminal, args):
        if not args:
            return
        pass