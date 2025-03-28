from password import Password

class Directory:
    def __init__(self, name, password = "", lockout_time = 0):
        self.name = name
        self.content = []

        if password:
            self.password = Password(password, lockout_time)
            self.has_password = True
        else:
            self.has_password = False

    # name methods
    def get_name(self):
        return self.name
    
    def rename(self, new_name):
        self.name = new_name

    # file methods
    def get_contents(self):
        return self.content
    
    def add_content(self, new_content):
        if new_content not in self.content:
            self.content.append(new_content)
    
    def ask_password(self, terminal):
        return self.password.enter_password(terminal)
