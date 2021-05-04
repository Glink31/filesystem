class Filesistem():
    def __init__(self):
        self.root = None
    def addroot(self,folder):
        self.root = folder
    def additem(self,item):
        if self.root is not None:
            self.root.additem(item)
        