class File():
    def __init__(self,name):
        self.name = name
    def copy(self):
        return File(self.name)
    def prnt(self,depth):
        for i in range (depth):
            print('-',end='')
        print(self.name)
