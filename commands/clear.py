from commands.command import Command

class Clear(Command):
    def execute(self, user, args):
        user.set_history([])