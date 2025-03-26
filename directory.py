class Directory:
    def __init__(self, name):
        self.name = name
        self.content = []

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