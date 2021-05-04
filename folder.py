class folder():
    def __init__(self,name):
        self.name = name
        self.contents = []
    def additem(self,item):
        self.contents.append(item)