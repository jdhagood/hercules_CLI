class User:
    def __init__(self, name, root):
        self.name = name
        self.working_dir = root
        self.path = [root]
        self.history = []

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name
    
    # path
    def get_path(self):
        return self.path
    
    def append_path(self, new_dir):
        self.path.append(new_dir)
    
    def pop_path(self):
        return self.path.pop()
    
    def set_path(self, path):
        self.path = path
    
    def get_working_dir(self):
        return self.path[-1]

    def get_path_str(self):
        path = self.get_name() + "@"
        for dir in self.path:
            path += dir.get_name() + "\\"

        path = path[0:-1] # remove last \
        return path
    
    def get_history(self):
        return self.history
    
    def append_history(self, new_history):
        self.history.append(new_history)

    def extend_history(self, new_history):
        self.history.extend(new_history)
    
    def get_terminal_string(self, command):
        return [(self.get_path_str(), "green"), (":~ $ ", "blue"), (command, "white")]