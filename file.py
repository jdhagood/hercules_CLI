class File:
    def __init__(self, name, extension, content = ""):
        self.name = name
        self.extension = extension
        self.content = content

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