from folder import Folder
class Filesystem():
    def __init__(self):
        self.root = Folder("C:")
    def additem(self,item):
        self.root.additem(item)
    def creatememento(self):
        return MementoReal(self.root.copy())
    def restore(self,memento):
        self.root = memento.state.copy