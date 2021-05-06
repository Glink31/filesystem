from memento import Memento
class MementoReal(Memento):
    def __init__(self,copy):
        self.state = copy
        
