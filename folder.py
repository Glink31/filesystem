class Folder():
    def __init__(self,name):
        self.name = name
        self.contents = []
    def additem(self,item):
        self.contents.append(item)
    def copy(self):
        f = Folder(self.name)
        for i in range (len(self.contents)):
            f.additem(self.contents[i])
        return f