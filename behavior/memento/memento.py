from abc import ABCMeta, abstractmethod


class IMemento(metaclass=ABCMeta):
    
        
    @abstractmethod
    def get_state(self):
        pass
    
    
class Memento(IMemento):
    
    def __init__(self, state):
        self.state = state
        
    def get_state(self):
        return self.state