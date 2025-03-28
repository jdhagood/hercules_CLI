from password import Password

class File:
    def __init__(self, name, extension, content = "", password = "", lockout_time = 0):
        self.name = name
        self.extension = extension
        self.content = content
        if password:
            self.password = Password(password, lockout_time)
            self.has_password = True
        else:
            self.has_password = False

    def get_name(self):
        return self.name

    def rename(self, new_name):
        self.name = new_name

    def get_extension(self):
        return self.extension

    
    def get_content(self):
        return self.content
    
    def set_content(self, new_content):
        self.content = new_content

    def is_protected(self):
        return self.has_password
    
    def ask_password(self, terminal):
        return self.password.enter_password(terminal)
