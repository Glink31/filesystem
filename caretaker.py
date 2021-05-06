class Caretaker():
    def __init__(self):
        self.states=[]

    def savestate(self,memento):
        self.atates.append(memento)

    def restorestate(self,n):
        return self.states[i]