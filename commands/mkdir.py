from commands.command import Command
from cli_objects.directory import Directory
class Mkdir(Command):
    def execute(self, user, args):
        if not args:
            return
        
        dir_name = args[0]
        working_dir = user.get_working_dir()
        for content in working_dir.get_contents():
            if isinstance(content, Directory) and content.get_name() == dir_name:
                user.append_history((f"'{dir_name}' already exists!\n\n", "red"))
                return

        working_dir.add_content(Directory(dir_name))