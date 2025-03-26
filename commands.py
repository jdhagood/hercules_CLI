import shlex
from directory import Directory
from file import File
from user import User

def cd(user, args):
    print('cd:', user.get_working_dir().name)
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
    


def clear(user, args):
    return ""

def ls(user, args):
    file_cat = []
    print('ls in:', user.get_working_dir().name)
    for file in user.get_working_dir().get_contents():
        if isinstance(file, File):
            file_cat.append((f"{file.get_name()}.{file.get_extension()}\n", "white"))
        elif isinstance(file, Directory):
            file_cat.append((f"{file.get_name()}\n", "blue"))

    file_cat.append(("\n", "white"))
    user.extend_history(file_cat)


def help(user, args):
    user.append_history(("lol, good luck XD\n\n", "white"))

hercules_commands = {
    "cd": cd,
    "clear": clear,
    "ls": ls,
    "help": help
}

def execute_command(command, user):

    user.extend_history(user.get_terminal_string(command))
    user.append_history(("\n", "white"))

    split_command = shlex.split(command)

    if split_command[0] in hercules_commands:
        hercules_commands[split_command[0]](user, split_command[1::])
    else:
        user.append_history((f"\n'{command}' is not recognized\n\n", "white"))