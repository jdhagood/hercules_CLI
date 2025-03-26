import shlex
import subprocess
import os

def execute_command(stdscr, command):
    global prompt
    stdscr.clear()
    args = shlex.split(command)

    if not args:
        return

    if args[0] == "cd":
        try:
            os.chdir(args[1] if len(args) > 1 else os.path.expanduser("~"))
        except Exception as e:
            stdscr.addstr(0, 0, f"cd: {e}")
    else:
        try:
            result = subprocess.run(args, capture_output=True, text=True, shell=True)
            stdscr.addstr(0, 0, result.stdout + result.stderr)
        except Exception as e:
            stdscr.addstr(0, 0, f"Error: {e}")