# command_manager.py
import shlex
import os
import importlib
from commands.command import Command

class CommandManager:
    def __init__(self):
        self.commands = {}
        self._load_commands()

    def _load_commands(self):
        # Dynamically import all modules in the 'commands' directory
        commands_dir = os.path.dirname(__file__) + "/commands"
        
        for filename in os.listdir(commands_dir):
            if filename.endswith(".py") and filename != "__init__.py":
                module_name = f"commands.{filename[:-3]}"  # Strip the ".py" extension
                module = importlib.import_module(module_name)
                
                # Look for any classes that inherit from Command
                for attribute_name in dir(module):
                    attribute = getattr(module, attribute_name)
                    if isinstance(attribute, type) and issubclass(attribute, Command):
                        print(attribute_name)
                        command_instance = attribute(attribute_name)
                        self.commands[attribute_name.lower()] = command_instance  # Register the command


    def execute(self, command, user):
        user.extend_history(user.get_terminal_string(command))
        user.append_history(("\n", "white"))

        split_command = shlex.split(command)
        command_name = split_command[0].lower()

        if command_name in self.commands:
            self.commands[command_name].execute(user, split_command[1::])
        else:
            user.append_history((f"Command '{command_name}' not recognized.\n\n", "red"))
