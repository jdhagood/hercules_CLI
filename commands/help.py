from commands.command import Command

class Help(Command):
    def execute(self, user, args):
        user.append_history(("lol, good luck XD\n\n", "white"))