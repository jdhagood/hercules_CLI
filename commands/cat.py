from commands.command import Command
from cli_objects.directory import Directory
from cli_objects.file import File

class Cat(Command):
    def execute(self, user, args, stdscr):
        if not args:
            return
        

        file_name = args[0]

        for object in user.get_working_dir().get_contents():
            if isinstance(object, File) and f"{object.get_name()}.{object.get_extension()}" == file_name:
                if object.is_protected() == True:
                    if object.ask_password(user, stdscr) == False:
                        return
                    
                user.append_history((object.get_content() + "\n\n", "white"))
                
                return
        
        user.append_history((f"{file_name} not found\n\n", "red"))