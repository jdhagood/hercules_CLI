from commands.command import Command
from cli_objects.directory import Directory

class Cd(Command):
    def execute(self, user, args):
        if not args:
            return
        
        new_dir = args[0]

        if new_dir == '..':
            if user.get_working_dir().get_name() != "root":
                user.pop_path()
                user.append_history(("\n", "white"))
            print('to:', user.get_working_dir().name)
            return

        for content in user.get_working_dir().get_contents():
            if isinstance(content, Directory) and content.get_name() == new_dir:
                user.append_path(content)
                user.append_history(("\n", "white"))
                print('to:', user.get_working_dir().name)
                return
        print('to:', user.get_working_dir().name)
        user.append_history(("The system cannot find the path specified.\n\n", "white"))