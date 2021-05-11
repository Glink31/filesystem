class Caretaker():
    def __init__(self):
        self.states=[]

    def savestate(self,memento):
        self.states.append(memento)

    def restorestate(self,n):
        return self.states[n]