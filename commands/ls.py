from commands.command import Command
from cli_objects.directory import Directory
from cli_objects.file import File

class Ls(Command):
    def execute(self, terminal, args):
        file_cat = []
        for file in terminal.user.get_working_dir().get_contents():
            if isinstance(file, File):
                file_cat.append((f"{file.get_name()}.{file.get_extension()}\n", "white"))
            elif isinstance(file, Directory):
                file_cat.append((f"{file.get_name()}\n", "blue"))

        file_cat.append(("\n", "white"))
        terminal.extend_history(file_cat)